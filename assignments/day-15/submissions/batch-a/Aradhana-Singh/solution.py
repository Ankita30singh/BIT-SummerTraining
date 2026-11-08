# Install the required libraries if needed:
# python3 -m pip install pandas numpy matplotlib scikit-learn joblib

# Start your program with:

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# Use this dataset:
customer_data = {
    "customer_id": list(range(1, 22)),
    "annual_income": [
        15, 18, 16, 22, 19, 14, 20,
        44, 48, 46, 52, 49, 45, 50,
        78, 82, 80, 88, 85, 76, 90,
    ],
    "spending_score": [
        20, 25, 18, 30, 22, 15, 28,
        48, 52, 50, 58, 55, 46, 53,
        82, 88, 78, 90, 85, 80, 92,
    ],
}

# ### Question 1: Load and Inspect the Data
# Create a DataFrame named `df` from `customer_data`.
df = pd.DataFrame(customer_data)
# Print:
# 1. the first five rows;
print(df.head(5))
# 2. the DataFrame shape;
print(df.shape)
# 3. the column names;
print(df.columns.tolist())
# 4. the missing-value count for each column.
print(df.isnull().sum())


# ### Question 2: Select the Clustering Features
# Create:
X = df[["annual_income", "spending_score"]]
# Print the first five rows of `X`.
print(X.head(5))
# In a comment, explain why `customer_id` should not be used as a clustering feature.
# customer_id should not be used because it is only a unique identifier and does not represent customer behaviour or characteristics.


# ### Question 3: Use the Elbow Method
inertias = []
# For every value of `k` from `1` to `7`:
# 1. create `KMeans(n_clusters=k, random_state=42, n_init=10)`;
# 2. train it with `X`;
# 3. add its `inertia_` value to a list named `inertias`.
for k in range(1, 8):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)

    inertias.append(model.inertia_)
# Print each `k` and inertia value rounded to two decimal places.
    print(f"k = {k}, Inertia = {model.inertia_:.2f}")
# Plot the inertia values against `k` using markers, axis labels, a title, and a grid. Save the chart as:

plt.figure(figsize=(7,5))
plt.plot(range(1,8), inertias, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
# Use `plt.tight_layout()` and `plt.close()` after saving.
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()


# ### Question 4: Train the Final K-Means Model
# Use three clusters:
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)

# Print the complete DataFrame and the number of customers in each cluster.
print(df)
print(df["cluster"].value_counts().sort_index())
# Add a comment explaining why cluster numbers such as `0`, `1`, and `2` are identifiers rather than rankings.
# Cluster numbers (0, 1, 2) are only labels assigned by K-Means and they are identifiers and do not represent any ranking or order.


# ### Question 5: Inspect the Centroids
# Get the cluster centres using:
centroids = model.cluster_centers_
# Print the centroids rounded to two decimal places. Clearly label the income and spending values in your output.
for i, center in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Annual Income = {center[0]:.2f}, "
        f"Spending Score = {center[1]:.2f}"
    )


# ### Question 6: Visualize Clusters and Centroids

# Create a scatter plot with:

# - annual income on the x-axis;
# - spending score on the y-axis;
# - customer points coloured by cluster;
# - centroids shown as large red `X` markers;
# - a title, axis labels, colour bar, and centroid legend.
plt.figure(figsize=(7,6))

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=80
)
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    color="red",
    marker="X",
    s=250,
    label="Centroids"
)
# Use `plt.tight_layout()` and `plt.close()` after saving.
plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.colorbar(scatter, label="Cluster")
plt.legend()

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()


# ### Question 7: Calculate the Silhouette Score
# Calculate:
score = silhouette_score(X, df["cluster"])
# Print the score rounded to three decimal places.
print(f"Silhouette Score: {score:.3f}")
# In a comment, explain that a higher silhouette score generally means points are closer to their own cluster and farther from other clusters.
# A higher silhouette score generally indicates that data points are closer to their own cluster and farther from other clusters.


# ### Question 8: Produce Business Insights
# Group the DataFrame by `cluster` and calculate the average annual income and spending score for each cluster.
summary = df.groupby("cluster")[["annual_income", "spending_score"]].mean()
print(summary)
# Print the summary table, then identify:
highest_spending = summary["spending_score"].idxmax()
highest_income = summary["annual_income"].idxmax()
discount_cluster = summary["spending_score"].idxmin()
premium_cluster = highest_spending

# Print one short reason for each marketing choice. Derive the cluster numbers from the summary instead of assuming a fixed label.
# 1. the cluster with the highest average spending score;
print(f"Cluster with Highest Average Spending Score: {highest_spending}")
print("Reason: Customers spend the most and respond well to premium products.")

# 2. the cluster with the highest average income;
print(f"Cluster with Highest Average Income: {highest_income}")
print("Reason: Customers have the highest purchasing power.")

# 3. a cluster that could receive discount offers;
print(f"Cluster for Discount Offers: {discount_cluster}")
print("Reason: Lower spending customers may be encouraged with discounts.")

# 4. a cluster that could receive premium-membership offers.
print(f"Cluster for Premium Membership Offers: {premium_cluster}")
print("Reason: High spending customers are suitable for premium memberships.")


# ### Question 9: Export the Model
# Save the trained model:
joblib.dump(model, "kmeans_model.pkl")
# Print:
print("Model saved as kmeans_model.pkl")
