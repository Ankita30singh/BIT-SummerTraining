sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]

# Question 1: Count Orders
print(f"Total orders: {len(sales)}")

# Question 2: Count Units Sold
total_units = sum(item["quantity"] for item in sales)
print(f"Total units sold: {total_units}")

# Question 3: Calculate Total Revenue
revenues = [item["price"] * item["quantity"] for item in sales]
print(f"Total revenue: {sum(revenues)}")

# Question 4: Filter Sales by City
gorakhpur_revenue = sum(item["price"] * item["quantity"] for item in sales if item["city"] == "Gorakhpur")
print(f"Gorakhpur revenue: {gorakhpur_revenue}")

# Question 5: Revenue by Category
revenue_by_category = {}
for item in sales:
    revenue_by_category.setdefault(item["category"], 0)
    revenue_by_category[item["category"]] += item["price"] * item["quantity"]
print(revenue_by_category)

# Question 6: Revenue by City
revenue_by_city = {}
for item in sales:
    revenue_by_city.setdefault(item["city"], 0)
    revenue_by_city[item["city"]] += item["price"] * item["quantity"]
print(revenue_by_city)

# Question 7: Best-Selling Product by Revenue
revenue_by_product = {}
for item in sales:
    revenue_by_product.setdefault(item["product"], 0)
    revenue_by_product[item["product"]] += item["price"] * item["quantity"]
best_product = max(revenue_by_product, key=revenue_by_product.get)
print(f"Top product: {best_product}")

# Question 8: High-Volume Products
high_volume_products = [item["product"] for item in sales if item["quantity"] >= 2]
print(high_volume_products)
