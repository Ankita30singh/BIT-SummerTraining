import csv
import os

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "sales_data.csv")

with open(DATA_FILE, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    records = [row for row in reader]

# Convert numeric values to integers
for row in records:
    row["price"] = int(row["price"])
    row["quantity"] = int(row["quantity"])

# Question 1: Read the CSV file
print(f"Total orders: {len(records)}")

# Question 2: Total units sold
total_units = sum(row["quantity"] for row in records)
print(f"Total units sold: {total_units}")

# Question 3: Total revenue
total_revenue = sum(row["price"] * row["quantity"] for row in records)
print(f"Total revenue: {total_revenue}")

# Question 4: Average order revenue
average_revenue = total_revenue / len(records)
print(f"Average order revenue: {average_revenue:.2f}")

# Question 5: Category revenue report
category_revenue = {}
for row in records:
    category_revenue.setdefault(row["category"], 0)
    category_revenue[row["category"]] += row["price"] * row["quantity"]
print(category_revenue)

# Question 6: City revenue report
city_revenue = {}
for row in records:
    city_revenue.setdefault(row["city"], 0)
    city_revenue[row["city"]] += row["price"] * row["quantity"]
print(city_revenue)

# Question 7: Top product
product_revenue = {}
for row in records:
    product_revenue.setdefault(row["product"], 0)
    product_revenue[row["product"]] += row["price"] * row["quantity"]

best_product = max(product_revenue, key=product_revenue.get)
print(f"Top product: {best_product}")

# Question 8: Gorakhpur orders
gorakhpur_orders = [row["order_id"] for row in records if row["city"] == "Gorakhpur"]
print(f"Gorakhpur order IDs: {gorakhpur_orders}")
