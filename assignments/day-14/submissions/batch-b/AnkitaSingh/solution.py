import numpy as np

customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

# Question 1: Understand the Data
print("Customer Data:", customers)
print("\nShape:", customers.shape)
print("Total number of customers:", customers.shape[0])

# This is an unsupervised-learning problem because no customer group
# (cluster) labels are provided. The algorithm must discover patterns
# and group similar customers on its own.


# Question 2: Calculate a Centroid

group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])

centroid = np.mean(group, axis=0)
print("\nCentroid of the group:",centroid)


# Question 3: Initial Centroids and Customer P

centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])

print("\nCentroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)


# Question 4: Euclidean Distance Function

def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

distance_a = euclidean_distance(customer_p, centroid_a)
distance_b = euclidean_distance(customer_p, centroid_b)

print("\nDistance from Customer P to Centroid A:", round(distance_a, 2))
print("Distance from Customer P to Centroid B:", round(distance_b, 2))


# Question 5: Assign Customer P

if distance_a < distance_b:
    print("\nCustomer P belongs to Cluster A")
else:
    print("\nCustomer P belongs to Cluster B")


# Question 6: Assign Every Customer

cluster_a = []
cluster_b = []

for customer in customers:
    dist_a = euclidean_distance(customer, centroid_a)
    dist_b = euclidean_distance(customer, centroid_b)

    if dist_a < dist_b:
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)

cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)

print("\nCluster A:")
print(cluster_a)

print("\nCluster B:")
print(cluster_b)


# Question 7: Recalculate the Centroids

new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)

print("\nNew Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))


# Question 8: Explain the K-Means Cycle

# Step 1: Find the nearest centroid for every data point.
# Step 2: Assign each data point to the closest cluster.
# Step 3: Calculate the new average (centroid) of each cluster.
# Step 4: Move the centroids to these new average positions.
# Step 5: Repeat the process until the cluster assignments stop changing.

print("\nK-Means may need several rounds because the centroids keep moving until the clusters become stable.")