import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import requests
    HAS_REQUESTS = True
except Exception:
    HAS_REQUESTS = False

OWID_CSV_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"


def download_owid_csv(url=OWID_CSV_URL, timeout=15):
    if not HAS_REQUESTS:
        raise RuntimeError("requests not installed")
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), parse_dates=["date"])


def make_sample_df():
    dates = pd.date_range("2020-01-01", periods=200)
    countries = ["World", "CountryA", "CountryB", "CountryC", "CountryD"]
    rows = []
    rng = np.random.default_rng(0)
    for country in countries:
        base = rng.integers(50, 500)
        cum = 0
        for d in dates:
            new_cases = max(0, int(rng.normal(loc=base, scale=base*0.5)))
            new_deaths = max(0, int(new_cases * rng.uniform(0.005, 0.03)))
            cum += new_cases
            rows.append({
                "iso_code": "XXX",
                "location": country,
                "date": d,
                "total_cases": cum,
                "new_cases": new_cases,
                "total_deaths": np.nan if new_deaths == 0 else new_deaths,  # not cumulative for sample
                "new_deaths": new_deaths,
                "population": 1_000_000
            })
    df = pd.DataFrame(rows)
    df = df.sort_values(["location", "date"])
    df["total_deaths"] = df.groupby("location")["new_deaths"].cumsum()
    return df


def load_data():
    print("Loading data...")
    try:
        df = download_owid_csv()
        print("Downloaded OWID data.")
    except Exception as e:
        print(
            f"Could not download OWID dataset (will use sample data). Reason: {e}")
        df = make_sample_df()
    if df['date'].dtype == object:
        df['date'] = pd.to_datetime(df['date'])
    return df


def prepare_summary(df):
    latest = df.sort_values("date").groupby(
        "location").tail(1).set_index("location")
    global_row = {
        "total_cases": latest["total_cases"].sum(skipna=True),
        "total_deaths": latest["total_deaths"].sum(skipna=True),
        "last_date": latest["date"].max()
    }
    return latest, global_row


def plot_country_timeseries(df, country="World", window=7, ax=None):
    s = df[df["location"] == country].sort_values("date")
    if s.empty:
        raise ValueError(f"No data for country '{country}'")
    s = s.set_index("date")
    s["new_cases"] = s["new_cases"].fillna(0)
    s["new_deaths"] = s["new_deaths"].fillna(0)
    s["total_cases"] = s["total_cases"].fillna(method="ffill").fillna(0)
    s["total_deaths"] = s["total_deaths"].fillna(method="ffill").fillna(0)

    ma_cases = s["new_cases"].rolling(window=window, min_periods=1).mean()
    ma_deaths = s["new_deaths"].rolling(window=window, min_periods=1).mean()

    if ax is None:
        fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    else:
        fig = None
        ax = np.array([ax, ax]) if not hasattr(ax, "__len__") else ax

    ax[0].bar(s.index, s["new_cases"], alpha=0.25, label="Daily new cases")
    ax[0].plot(s.index, ma_cases, linewidth=2,
               label=f"{window}-day MA (cases)")
    ax[0].set_ylabel("New cases")
    ax[0].set_title(f"{country} — Daily New Cases (rolling {window})")
    ax[0].legend()

    ax[1].bar(s.index, s["new_deaths"], alpha=0.25, label="Daily new deaths")
    ax[1].plot(s.index, ma_deaths, linewidth=2,
               label=f"{window}-day MA (deaths)")
    ax[1].set_ylabel("New deaths")
    ax[1].set_title(f"{country} — Daily New Deaths (rolling {window})")
    ax[1].legend()

    plt.tight_layout()
    return fig


def plot_top_countries_bar(latest_df, top_n=10, value_col="total_cases"):
    to_exclude = ["World", "International"]
    candidates = latest_df[~latest_df.index.isin(to_exclude)].dropna(subset=[
        value_col], how="all")
    top = candidates.sort_values(value_col, ascending=False).head(top_n)
    fig, ax = plt.subplots(figsize=(10, max(4, top_n * 0.4)))
    ax.barh(top.index[::-1], top[value_col].astype(float)[::-1])
    ax.set_xlabel(value_col.replace("_", " ").title())
    ax.set_title(f"Top {len(top)} countries by {value_col.replace('_',' ')}")
    plt.tight_layout()
    return fig


def show_top_table(latest_df, top_n=10, value_col="total_cases"):
    candidates = latest_df.dropna(subset=[value_col], how="all")
    top = candidates.sort_values(value_col, ascending=False).head(top_n)[
        [value_col, "population"]]
    top = top.assign(cases_per_100k=(
        top[value_col] / top["population"]) * 100000)
    return top


def main():
    df = load_data()
    cols_needed = ["iso_code", "location", "date", "total_cases",
                   "new_cases", "total_deaths", "new_deaths", "population"]
    present = [c for c in cols_needed if c in df.columns]
    df = df[present].copy()

    latest_df, global_summary = prepare_summary(df)

    print("\n=== GLOBAL SUMMARY ===")
    print(
        f"Last date in dataset: {pd.to_datetime(global_summary['last_date']).date()}")
    print(
        f"Global total cases (sum of latest rows): {int(global_summary['total_cases']):,}")
    print(
        f"Global total deaths (sum of latest rows): {int(global_summary['total_deaths']):,}")

    top_n = 10
    top_table = show_top_table(latest_df, top_n=top_n, value_col="total_cases")
    print(f"\nTop {top_n} countries by total cases:\n")
    print(top_table.to_string(float_format='{:,.0f}'.format))
    fig1 = plot_top_countries_bar(
        latest_df, top_n=top_n, value_col="total_cases")
    fig1.show()
    country_to_plot = "World"
    if country_to_plot not in df["location"].unique():
        country_to_plot = latest_df["total_cases"].astype(float).idxmax()

    fig2 = plot_country_timeseries(df, country=country_to_plot, window=7)
    fig2.show()
    top5 = latest_df.sort_values(
        "total_cases", ascending=False).head(5).index.tolist()
    plt.figure(figsize=(12, 6))
    for loc in top5:
        s = df[df["location"] == loc].sort_values("date").set_index("date")
        if "new_cases" not in s:
            continue
        ma = s["new_cases"].rolling(7, min_periods=1).mean()
        plt.plot(ma.index, ma.values, label=loc)
    plt.title("7-day rolling average — New cases (Top 5 countries)")
    plt.xlabel("Date")
    plt.ylabel("New cases (7-day MA)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
