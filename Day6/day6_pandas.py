import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("Day6/sales_data_sample.csv", encoding="latin1")
# # print(df)
# print("info data")
# print(df.info())

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Zain"],
    "Class": ["10th", "10th", "9th", "9th", "8th"],
    "Marks": [85, 92, 78, 88, 90],
    "Gender": ["M", "F", "M", "F", "M"]
}

df = pd.DataFrame(data)
# print(df.head(3))
print(df.shape)
# print(df.columns)


# print(df.iloc[0])
# print(df.iloc[0:3])
# print(df.iloc[:, 0])
# print(df.iloc[0:3, 0:2])

print(df.loc[0])
print(df.loc[:, ["Name", "Marks"]])
print(df.loc[df["Marks"] > 85])
print(df.loc[df["Gender"] == "F", ["Name", "Marks"]])

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].fillna("Unknown")
print(df)

# renaming
df = df.rename(columns={"Marks": "Score", "Class": "Grade"})
print(df)

#
# df1 = df.drop(columns=["Gender"])
# print(df1)

#
# df2 = df.drop(index=3)
# print(df2)

# Sorting
print(df.sort_values(by="Score"))
print(df.sort_values(by="Score", ascending=False))
print(df.sort_values(by=["Grade", "Score"]))

# Grouping
df.groupby(['Name', 'Grade'])['Score'].mean()

df["Gender"].value_counts()
