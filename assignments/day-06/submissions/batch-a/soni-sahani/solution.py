#assignment 6

# Use this sales data in your program:

# sales = [
#     {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
#     {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
#     {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
#     {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
#     {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
#     {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
# ]
#For each record, revenue means:revenue = price * quantity


#Question 1: Count Orders(Print the total number of sales records.)
# Expected Output:Total orders: 6
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]
print("Total orders:", len(sales))


#Question 2: Count Units Sold(Calculate and print the total quantity sold across all records.)
# Expected Output:Total units sold: 10
# Question 2: Count Units Sold (using for loop)
total_units = 0
for record in sales:
    total_units += record["quantity"]

print("Total units sold:", total_units)


#Question 3: Calculate Total Revenue(Calculate and print the total revenue from all sales records.)
# Expected Output:Total revenue: 10690
total_revenue = 0
for record in sales:
    total_revenue += record["price"] * record["quantity"]

print("Total revenue:", total_revenue)



#Question 4: Filter Sales by City(Calculate the total revenue for sales where the city is "Gorakhpur".)
# Expected Output:Gorakhpur revenue: 7393

gorakhpur_revenue = 0
for record in sales:            
    if record["city"] == "Gorakhpur":
        gorakhpur_revenue += record["price"] * record["quantity"]
print("Gorakhpur revenue:", gorakhpur_revenue)


#Question 5: Revenue by Category(Create a dictionary that stores total revenue for each category and print it.)
# Expected Output:{'Online Course': 7494, 'Workshop': 3196}
category_revenue = {}
for record in sales:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)



#Question 6: Revenue by City(Create a dictionary that stores total revenue for each city and print it.)
# Expected Output:{'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}

revenue_by_city = {}

for record in sales:
    city = record["city"]
    revenue = record["price"] * record["quantity"]
    if city in revenue_by_city:
        revenue_by_city[city] += revenue
    else:
        revenue_by_city[city] = revenue

print(revenue_by_city)



#Question 7: Best-Selling Product by Revenue(Find the product with the highest total revenue and print its name.)
# Expected Output:Top product: Data Analytics Course
revenue_by_product = {}

for record in sales:
    product = record["product"]
    revenue = record["price"] * record["quantity"]
    if product in revenue_by_product:
        revenue_by_product[product] += revenue
    else:
        revenue_by_product[product] = revenue
top_product = max(revenue_by_product, key=revenue_by_product.get)
print("Top product:", top_product)





#Question 8: High-Volume Products(Create a list of product names for records where quantity is 2 or more. Keep the same order as the original data and print the list.)
# Expected Output:['Python Course', 'AI Workshop', 'Data Analytics Course']
high_volume_products = []

for item in sales:
    if item["quantity"] >= 2:
        high_volume_products.append(item["product"])

print(high_volume_products)
