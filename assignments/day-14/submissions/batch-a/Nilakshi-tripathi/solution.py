import numpy as np

# Question 1: Understand Data
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

print("Customers Data:\n", customers)
print("Shape:", customers.shape)
print("Total customers:", customers.shape[0])

# This is an unsupervised learning problem because there are no labels
# (no predefined groups). We are trying to discover hidden patterns.

# Question 2: Calculate Centroid
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])

centroid = np.mean(group, axis=0)
print("\nCentroid:", centroid)

# Question 3: Initial Centroids
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])

print("\nCentroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)

# Question 4: Euclidean Distance
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

dist_a = euclidean_distance(customer_p, centroid_a)
dist_b = euclidean_distance(customer_p, centroid_b)

print("\nDistance to Centroid A:", round(dist_a, 2))
print("Distance to Centroid B:", round(dist_b, 2))

# Question 5: Assign Customer P
if dist_a < dist_b:
    print("\nCustomer P belongs to Cluster A")
else:
    print("\nCustomer P belongs to Cluster B")

# Question 6: Assign Every Customer
cluster_a = []
cluster_b = []

for customer in customers:
    d_a = euclidean_distance(customer, centroid_a)
    d_b = euclidean_distance(customer, centroid_b)

    if d_a < d_b:
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)

cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)

print("\nCluster A:\n", cluster_a)
print("Cluster B:\n", cluster_b)

# Question 7: Recalculate Centroids
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)

print("\nNew Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))

# Question 8: Explanation
# Find the nearest centroid
# Assign points to groups
# Calculate each group's new average
# Move the centroids
# Repeat until the groups stop changing
#
# K-Means needs several rounds because centroids keep adjusting
# until the clusters become stable (no more changes).