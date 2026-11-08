import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# Customer Dataset
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


# Question 1
df = pd.DataFrame(customer_data)
print("First Five Rows:", df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nMissing Values:",df.isnull().sum())



# Question 2
X = df[["annual_income", "spending_score"]]

print("\nSelected Features:")
print(X.head())

# customer_id is only a unique identifier.
# It does not describe customer behaviour, so it should
# not be used for clustering.


# Question 3
inertias = []

print("\nElbow Method")

for k in range(1, 8):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)

    inertias.append(model.inertia_)
    print(f"k = {k}, Inertia = {model.inertia_:.2f}")

plt.figure(figsize=(6, 4))
plt.plot(range(1, 8), inertias, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)

plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()


# Question 4

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = model.fit_predict(X)

print("\nDataFrame with Clusters:")
print(df)
print("\nCustomers in Each Cluster:")
print(df["cluster"].value_counts())

# Cluster labels such as 0, 1 and 2 are only identifiers.
# They do not indicate better or worse clusters.


# Question 5

centroids = model.cluster_centers_
print("\nCentroids")

for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Income = {centroid[0]:.2f}, "
        f"Spending = {centroid[1]:.2f}"
    )

# Question 6

plt.figure(figsize=(7, 5))

plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=80
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    marker="X",
    s=250,
    label="Centroids"
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Clusters")
plt.colorbar(label="Cluster")
plt.legend()

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()

# Question 7

score = silhouette_score(X, df["cluster"])

print(f"\nSilhouette Score: {score:.3f}")

# A higher silhouette score generally means customers
# are closer to their own cluster and farther from
# customers in other clusters.

# Question 8

summary = df.groupby("cluster")[
    ["annual_income", "spending_score"]
].mean()

print("\nCluster Summary")
print(summary)

highest_spending = summary["spending_score"].idxmax()
highest_income = summary["annual_income"].idxmax()
lowest_spending = summary["spending_score"].idxmin()

print(
    f"\nHighest average spending: Cluster {highest_spending}"
)
print("Reason: Customers spend the most and are ideal for premium promotions.")

print(
    f"\nHighest average income: Cluster {highest_income}"
)
print("Reason: Customers have the highest purchasing power.")

print(
    f"\nDiscount Offers: Cluster {lowest_spending}"
)
print("Reason: Lower spending customers may respond well to discounts.")

print(
    f"\nPremium Membership: Cluster {highest_spending}"
)
print("Reason: High-spending customers are strong candidates for premium membership.")


# Question 9

joblib.dump(model, "kmeans_model.pkl")
print("\nModel saved as kmeans_model.pkl")