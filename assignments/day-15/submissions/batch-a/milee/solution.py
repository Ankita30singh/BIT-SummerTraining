import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# -----------------------------
# Dataset
# -----------------------------
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

# ==================================================
# Question 1: Load and Inspect the Data
# ==================================================

df = pd.DataFrame(customer_data)

print("First five rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

# ==================================================
# Question 2: Select the Clustering Features
# ==================================================

X = df[["annual_income", "spending_score"]]

print("\nFirst five rows of X:")
print(X.head())

# customer_id should not be used because it is only a unique identifier
# and does not represent customer behaviour or characteristics.

# ==================================================
# Question 3: Use the Elbow Method
# ==================================================

inertias = []

print("\nElbow Method Results:")

for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    print(f"k = {k}, Inertia = {kmeans.inertia_:.2f}")

plt.figure(figsize=(6, 4))
plt.plot(range(1, 8), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()

# ==================================================
# Question 4: Train the Final K-Means Model
# ==================================================

model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)

print("\nComplete DataFrame:")
print(df)

print("\nCustomers in each cluster:")
print(df["cluster"].value_counts().sort_index())

# Cluster labels such as 0, 1, and 2 are simply identifiers.
# They do not represent any ranking or ordering.

# ==================================================
# Question 5: Inspect the Centroids
# ==================================================

centroids = model.cluster_centers_

print("\nCluster Centroids:")

for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Annual Income = {centroid[0]:.2f}, "
        f"Spending Score = {centroid[1]:.2f}"
    )

# ==================================================
# Question 6: Visualize Clusters and Centroids
# ==================================================

plt.figure(figsize=(7, 5))

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=80,
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color="red",
    marker="X",
    s=250,
    label="Centroids",
)

plt.title("Customer Segments using K-Means")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(scatter, label="Cluster")
plt.legend()

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()

# ==================================================
# Question 7: Calculate the Silhouette Score
# ==================================================

score = silhouette_score(X, df["cluster"])

print(f"\nSilhouette Score: {score:.3f}")

# A higher silhouette score generally indicates that points are closer
# to their own cluster and farther away from other clusters.

# ==================================================
# Question 8: Produce Business Insights
# ==================================================

summary = (
    df.groupby("cluster")[["annual_income", "spending_score"]]
    .mean()
    .round(2)
)

print("\nCluster Summary:")
print(summary)

highest_spending_cluster = summary["spending_score"].idxmax()
highest_income_cluster = summary["annual_income"].idxmax()
lowest_spending_cluster = summary["spending_score"].idxmin()

print(
    f"\nCluster with highest average spending score: {highest_spending_cluster}"
)
print("Reason: Customers spend the most and are valuable buyers.")

print(
    f"\nCluster with highest average income: {highest_income_cluster}"
)
print("Reason: Customers have the highest purchasing power.")

print(
    f"\nCluster for discount offers: {lowest_spending_cluster}"
)
print("Reason: Lower spending customers may respond to discounts.")

print(
    f"\nCluster for premium membership offers: {highest_income_cluster}"
)
print("Reason: High-income customers are more likely to buy premium services.")

# ==================================================
# Question 9: Export the Model
# ==================================================

joblib.dump(model, "kmeans_model.pkl")

print("\nModel saved as kmeans_model.pkl")