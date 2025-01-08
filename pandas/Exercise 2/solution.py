import pandas as pd
df = pd.read_csv("2-fruits_data.csv")
rows, columns = df.shape
print(f"No of rows: {rows}\nNo of columns: {columns}\n")
print(f"Name of columns: {", ".join(list(df.columns))}\n")
print(df.to_string())
print("\n")

new_df = df.fillna(-1)
print(new_df.to_string())

New_df = df.copy()
New_df["apple(1kg)"] = New_df["apple(1kg)"].fillna(New_df["apple(1kg)"].mean())
New_df["banana(1 dozen)"] = New_df["banana(1 dozen)"].fillna(New_df["banana(1 dozen)"].mean())
New_df["grapes(1kg)"] = New_df["grapes(1kg)"].fillna(New_df["grapes(1kg)"].median())
New_df["mango(1kg)"] = New_df["mango(1kg)"].fillna(New_df["mango(1kg)"].median())
New_df["Water Melons(1)"] = New_df["Water Melons(1)"].fillna("Not available")

print("\n")
print(New_df.to_string())

New_df1 = df.ffill()
print("\n")
print(New_df1.to_string())

New_df2 = df.dropna(thresh=4)
print("\n")
print(New_df2.to_string())

new_df3 = df.dropna()
print("\n")
print(new_df3.to_string())
new_df3.to_csv("2-fruits_data.csv", index=False)
