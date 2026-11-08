# Question 1: Count Orders
# Print the total number of sales records.

sales_records = [
    {"id": 1, "product": "Data Science","Category": "Workshop", "quantity": 2, "price": 1000,"City":"Delhi"},
    {"id": 2, "product": "Data Analysis", "Category": "Online", "quantity": 5, "price": 25,"City":"Gorakhpur"},
    {"id": 3, "product": "Data Visualization", "Category": "Workshop", "quantity": 4, "price": 433,"City":"Bangalore"},
    {"id": 4, "product": "Data Analysis", "Category": "Online", "quantity": 2, "price": 300,"City":"Chennai"},
    {"id": 5, "product": "AI Course", "Category": "Workshop", "quantity": 4, "price": 100,"City":"Gorakhpur"},
    {"id": 6, "product": "Data Science", "Category": "Workshop", "quantity": 1, "price": 50,"City":"Pune"}
]
print("Total orders:", len(sales_records))

# Question 2: Count Units Sold

total_units_sales = sum(record["quantity"] for record in sales_records)
print("Total units sold:", total_units_sales)

# Question 3: Calculate Total Revenue
# Calculate and print the total revenue from all sales records.

total_revenue = sum(record["quantity"] * record["price"] for record in sales_records)
print("Total revenue:", total_revenue)

# Question 4: Filter Sales by City
# Calculate the total revenue for sales where the city is `"Gorakhpur"`

gorakhpur_revenue = sum(record["quantity"] * record["price"] for record in sales_records)
print("Gorakhpur revenue:", gorakhpur_revenue)

# Question 5: Filter Sales by Category
# Calculate the total revenue for sales where the category is `"Electronics"`

category_revenue = {}
for record in sales_records:
    category = record["Category"]
    revenue = record["quantity"] * record["price"]
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print("Sales by category:", category_revenue)

# Question 6: Revenue by City
# Create a dictionary that stores total revenue for each city and print it.

City_revenue = {}
for record in sales_records:
    city = record["City"]
    revenue = record["quantity"] * record["price"]
    if city in City_revenue:
        City_revenue[city] += revenue
    else:
        City_revenue[city] = revenue
print("Sales by city:", City_revenue)

# Best-Selling Product by Revenue
# Find the product with the highest total revenue and print its name.
# ```python
# Expected Output:
# Top product: Data Analytics Course
product_revenue = {}
for record in sales_records:
    product = record["product"]
    revenue = record["quantity"] * record["price"]
    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = max(product_revenue, key=lambda x: product_revenue[x])
print("Top product:", top_product)

# Question 8: High-Volume Products

high_volume_products = [record["product"] for record in sales_records if record["quantity"] > 3]
print("High-volume products:", high_volume_products)