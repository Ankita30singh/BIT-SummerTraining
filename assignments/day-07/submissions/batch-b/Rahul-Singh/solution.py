import csv

# Read CSV file
data = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        data.append(row)


# Question 1: Total Orders

total_orders = len(data)
print("Total orders:", total_orders)


# Question 2: Total Units Sold


total_units = 0

for row in data:
    total_units += row["quantity"]

print("Total units sold:", total_units)


# Question 3: Total Revenue


total_revenue = 0

for row in data:
    revenue = row["price"] * row["quantity"]
    total_revenue += revenue

print("Total revenue:", total_revenue)


# Question 4: Average Order Revenue


average_revenue = total_revenue / total_orders

print("Average order revenue:", round(average_revenue, 2))


# Question 5: Revenue by Category

category_revenue = {}

for row in data:
    category = row["category"]
    revenue = row["price"] * row["quantity"]

    if category not in category_revenue:
        category_revenue[category] = 0

    category_revenue[category] += revenue

print(category_revenue)


# Question 6: Revenue by City


city_revenue = {}

for row in data:
    city = row["city"]
    revenue = row["price"] * row["quantity"]

    if city not in city_revenue:
        city_revenue[city] = 0

    city_revenue[city] += revenue

print(city_revenue)


# Question 7: Top Product


product_revenue = {}

for row in data:
    product = row["product"]
    revenue = row["price"] * row["quantity"]

    if product not in product_revenue:
        product_revenue[product] = 0

    product_revenue[product] += revenue

top_product = ""
max_revenue = 0

for product in product_revenue:
    if product_revenue[product] > max_revenue:
        max_revenue = product_revenue[product]
        top_product = product

print("Top product:", top_product)


# Question 8: Gorakhpur Orders

gorakhpur_orders = []

for row in data:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)