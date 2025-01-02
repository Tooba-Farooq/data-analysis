import pandas as pd
df = pd.read_csv("1-bengaluru_house_prices.csv")
row, column = df.shape
print(f"Number of rows: {row}\nNumber of columns: {column}\n")
top_5_rows = df.head()
print(f"Top 5 rows:\n{top_5_rows}\n")

area_type_categories = df["area_type"].unique()
size_categories = df["size"].unique()
print(f"Unique categories present in area_type column are: {area_type_categories}")
print(f"Unique categories present in size column are: {size_categories}\n")

super_built_up_with_2_BHK = df[(df["area_type"] == 'Super built-up  Area') & (df["size"] == '2 BHK')]
count = super_built_up_with_2_BHK.shape[0]
print(f"No of houses with super built-up area and with 2 Bedroom, 1 Hall and Kitchen are: {count}\n")

df["price_category"] = df["price"].apply(lambda x:"Affordable" if x < 80 else "High cost")
print(f"Updated data frame with price_category column:\n{df.head().to_string()}\n")

greater_than_average_price = df[df["price"] > df["price"].mean()]
print(f"Houses that have prices greater than mean/average price of all houses:\n{greater_than_average_price.to_string()}")