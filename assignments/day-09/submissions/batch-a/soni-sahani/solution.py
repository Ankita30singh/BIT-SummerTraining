#assignment 9
# Use this data to create a DataFrame:

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}

#Question 1: Create and Print a DataFrame(Create a DataFrame named df from sales_data. Print the DataFrame.)

import pandas as pd
df = pd.DataFrame(sales_data)
print(df)


#Question 2: Inspect the Data(Print the number of rows and columns in this format:)
# Expected Output:
# Rows: 6
# Columns: 5

rows, cols = df.shape
print("Rows:", rows)
print("Columns:", cols)

#Question 3: Add Revenue Column(Create a revenue column using price * quantity. Print only the product and revenue columns.)

df["revenue"] = df["price"] * df["quantity"]
print(df[["product", "revenue"]])


#Question 4: Total Revenue(Calculate and print the total revenue.)
# Expected Output:
# Total revenue: 10690

df["revenue"] = df["price"] * df["quantity"]
total_revenue = df["revenue"].sum()
print("Total revenue:", total_revenue)


#Question 5: Filter Gorakhpur Sales(Create a new DataFrame containing rows where the city is Gorakhpur. Print its product, quantity, and revenue columns.)

df["revenue"] = df["price"] * df["quantity"]
gorakhpur_sales = df[df["city"] == "Gorakhpur"]
print(gorakhpur_sales[["product", "quantity", "revenue"]])


#Question 6: Revenue by Category(Use groupby to calculate and print total revenue by category.)
# Expected Values:
# Online Course: 7494
# Workshop: 3196

df["revenue"] = df["price"] * df["quantity"]
revenue_by_category = df.groupby("category")["revenue"].sum()
print(revenue_by_category)


#Question 7: Revenue by CityUse groupby to calculate and print total revenue by city.
# Expected Values:
# Deoria: 999
# Gorakhpur: 7393
# Lucknow: 2298

df["revenue"] = df["price"] * df["quantity"]
revenue_by_city = df.groupby("city")["revenue"].sum()
print(revenue_by_city)


#Question 8: Top Revenue Product(Group the data by product, find the product with the highest total revenue, and print it.)
# Expected Output:Top product: Data Analytics Course

df["revenue"] = df["price"] * df["quantity"]
product_revenue = df.groupby("product")["revenue"].sum()
top_product = product_revenue.idxmax()
print("Top product:", top_product)


