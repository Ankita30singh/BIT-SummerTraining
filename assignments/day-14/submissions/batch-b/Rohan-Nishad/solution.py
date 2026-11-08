import numpy as np

# Question 1: Understand the Data
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])
print(customers)
print(f"Shape: {customers.shape}")
print(f"Total customers: {customers.shape[0]}")

# This is unsupervised learning because we do not have labels for the customer groups.
# The algorithm must find the groups based on the data alone.

# Question 2: Calculate a Centroid
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])
centroid_group = np.mean(group, axis=0)
print(centroid_group)

# Question 3: Initial Centroids and Customer P
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])
print(centroid_a)
print(centroid_b)
print(customer_p)

# Question 4: Euclidean Distance Function
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

distance_a = euclidean_distance(customer_p, centroid_a)
distance_b = euclidean_distance(customer_p, centroid_b)
print(f"{distance_a:.2f}")
print(f"{distance_b:.2f}")

# Question 5: Assign Customer P
if distance_a < distance_b:
    print("Customer P belongs to Cluster A")
else:
    print("Customer P belongs to Cluster B")

# Question 6: Assign Every Customer
cluster_a = []
cluster_b = []
for customer in customers:
    dist_a = euclidean_distance(customer, centroid_a)
    dist_b = euclidean_distance(customer, centroid_b)
    if dist_a <= dist_b:
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)

cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)
print(cluster_a)
print(cluster_b)

# Question 7: Recalculate the Centroids
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)
print(np.round(new_centroid_a, 2))
print(np.round(new_centroid_b, 2))

# Question 8: Explain the K-Means Cycle
# Find the nearest centroid for each point.
# Assign points to the group with the closest centroid.
# Calculate each group's new average position.
# Move the centroids to the new averages.
# Repeat until the groups stop changing.

print("K-means may need several rounds because centroids move and assignments can change after each update.")
