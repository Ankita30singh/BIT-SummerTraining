# order_id,product,category,price,quantity,city
# ORD-001,Python Course,Online Course,999,2,Gorakhpur
# ORD-002,Data Analytics Course,Online Course,1499,1,Lucknow
# ORD-003,AI Workshop,Workshop,799,3,Gorakhpur
# ORD-004,Python Course,Online Course,999,1,Deoria
# ORD-005,Data Analytics Course,Online Course,1499,2,Gorakhpur
# ORD-006,AI Workshop,Workshop,799,1,Lucknow

# Question 1: Read the CSV File
# Read all rows from `sales_data.csv` and print the total number of orders.
import csv
import os
with open('sales_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["order_id", "product", "category", "price", "quantity", "city"])
    writer.writeheader()
    writer.writerow({"order_id": "ORD-001", "product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"})
    writer.writerow({"order_id": "ORD-002", "product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"})
    writer.writerow({"order_id": "ORD-003", "product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"})
    writer.writerow({"order_id": "ORD-004", "product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"})
    writer.writerow({"order_id": "ORD-005", "product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"})
    writer.writerow({"order_id": "ORD-006", "product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"})
    
with open('sales_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    orders = list(reader)
    print(f"Total number of orders: {len(orders)}")
    
# Question 2: Total Units Sold

with open('sales_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    total_units_sold = sum(int(record['quantity']) for record in reader)
    print(f"Total units sold: {total_units_sold}")
    
# Question 3: Total Revenue
with open("sales_data.csv", 'r') as f:
    reader = csv.DictReader(f)
    Total_revenue = sum(int(record["price"]) * int(record["quantity"]) for record in reader)
    print(f"Total revenue: {Total_revenue}")
    
# Question 4: Average Order Revenue
# Calculate total revenue divided by total orders. Round the result to 2 decimal places.
# Expected Output:
# Average order revenue: 1781.67
with open("sales_data.csv", 'r') as f:
    reader = csv.DictReader(f)
    total_revenue = sum(int(record["price"]) * int(record["quantity"]) for record in reader)
    total_orders = len(orders)
    average_order_revenue = round(total_revenue / total_orders, 2)
    print(f"Average order revenue: {average_order_revenue}")

# # Question 5: Category Revenue Report
# Create and print a dictionary of total revenue by category.
with open("sales_data.csv", "r") as f:
    reader = csv.DictReader(f)
    category_revenue = {}
    for record in reader:
        category = record["category"]
        revenue = int(record["price"]) * int(record["quantity"])
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue
print(f"Category revenue report: {category_revenue}")

# Question 6: City Revenue Report
with open("sales_data.csv", "r") as f:
    reader = csv.DictReader(f)
    city_revenue = {}
    for record in reader:
        city = record["city"]
        revenue = int(record["price"]) * int(record["quantity"])
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue
print("City revenue report:", city_revenue)

# Question 7: Top Product
# Find the product with the highest total revenue and print it.
with open("sales_data.csv", "r") as f:
    reader = csv.DictReader(f)
    product_revenue = {}
    for record in reader:
        product = record["product"]
        revenue = int(record["price"]) * int(record["quantity"])
        if product in product_revenue:
            product_revenue[product] += revenue
        else:   
            product_revenue[product] = revenue
print("Top product:", max(product_revenue, key=lambda x: product_revenue[x]))

# Question 8: Gorakhpur Orders
# Create a list of `order_id` values where the city is `"Gorakhpur"`. Keep the CSV order and print the list.
# code line by line
with open("sales_data.csv", "r") as f:
    reader = csv.DictReader(f)
    gorakhpur_orders = [record["order_id"] for record in reader if record["city"] == "Gorakhpur"]
print("Gorakhpur orders:", gorakhpur_orders)