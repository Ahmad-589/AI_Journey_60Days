import pandas as pd

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

print("Downloading OWID COVID-19 dataset...")
df = pd.read_csv(url)
print("Download complete!")
print("Rows:", df.shape[0], " Columns:", df.shape[1])
print("\nPreview:")
print(df.head())
