import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Dataset
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

print("First Five Rows:")
print(df.head())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Question 2
# customer_id is only an identifier and should not be used for clustering.
X = df[["annual_income", "spending_score"]]

print("\nFeatures:")
print(X.head())

# Question 3
inertias = []

print("\nElbow Method")
for k in range(1, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)
    print(f"k={k} Inertia={km.inertia_:.2f}")

plt.figure(figsize=(6,4))
plt.plot(range(1,8), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()

# Question 4
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)

print("\nClustered Data:")
print(df)

print("\nCustomers in each Cluster:")
print(df["cluster"].value_counts())

# Cluster numbers are identifiers, not rankings.

# Question 5
centroids = model.cluster_centers_

print("\nCentroids")
for i, c in enumerate(centroids):
    print(f"Cluster {i}: Income={c[0]:.2f}, Spending={c[1]:.2f}")

# Question 6
plt.figure(figsize=(6,5))

plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=70
)

plt.scatter(
    centroids[:,0],
    centroids[:,1],
    color="red",
    marker="X",
    s=250,
    label="Centroids"
)

plt.title("Customer Clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(label="Cluster")
plt.legend()

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()

# Question 7
score = silhouette_score(X, df["cluster"])

print(f"\nSilhouette Score: {score:.3f}")

# Higher silhouette score means better separated clusters.

# Question 8
summary = df.groupby("cluster")[["annual_income","spending_score"]].mean()

print("\nCluster Summary")
print(summary)

highest_spending = summary["spending_score"].idxmax()
highest_income = summary["annual_income"].idxmax()
lowest_spending = summary["spending_score"].idxmin()

print(f"\nHighest Spending Cluster: {highest_spending}")
print("Reason: Customers spend the most.")

print(f"\nHighest Income Cluster: {highest_income}")
print("Reason: Customers have the highest income.")

print(f"\nDiscount Offer Cluster: {lowest_spending}")
print("Reason: Lower spending customers can be encouraged with discounts.")

print(f"\nPremium Membership Cluster: {highest_spending}")
print("Reason: High spending customers are suitable for premium membership.")

# Question 9
joblib.dump(model, "kmeans_model.pkl")

print("\nModel saved as kmeans_model.pkl")