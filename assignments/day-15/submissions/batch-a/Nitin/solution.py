import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# -------------------------------
# Dataset
# -------------------------------
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

# -------------------------------
# Question 1
# -------------------------------
df = pd.DataFrame(customer_data)

print("First Five Rows:")
print(df.head())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
# Question 2
# -------------------------------
X = df[["annual_income", "spending_score"]]

print("\nSelected Features:")
print(X.head())

# customer_id is only an identifier and should not be used for clustering.

# -------------------------------
# Question 3
# -------------------------------
inertias = []

print("\nElbow Method:")

for k in range(1, 8):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertias.append(model.inertia_)
    print(f"k={k} Inertia={model.inertia_:.2f}")

plt.figure(figsize=(6,4))
plt.plot(range(1,8), inertias, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()

# -------------------------------
# Question 4
# -------------------------------
model = KMeans(n_clusters=3, random_state=42, n_init=10)

df["cluster"] = model.fit_predict(X)

print("\nComplete DataFrame:")
print(df)

print("\nCustomers in each cluster:")
print(df["cluster"].value_counts())

# Cluster labels (0,1,2) are identifiers, not rankings.

# -------------------------------
# Question 5
# -------------------------------
centroids = model.cluster_centers_

print("\nCentroids:")

for i, c in enumerate(centroids):
    print(
        f"Cluster {i}: Income = {c[0]:.2f}, Spending = {c[1]:.2f}"
    )

# -------------------------------
# Question 6
# -------------------------------
plt.figure(figsize=(7,5))

plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=80,
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

# -------------------------------
# Question 7
# -------------------------------
score = silhouette_score(X, df["cluster"])

print("\nSilhouette Score:", round(score,3))

# Higher silhouette score means better separated clusters.

# -------------------------------
# Question 8
# -------------------------------
summary = df.groupby("cluster")[["annual_income","spending_score"]].mean()

print("\nCluster Summary:")
print(summary)

highest_spending = summary["spending_score"].idxmax()
highest_income = summary["annual_income"].idxmax()
lowest_spending = summary["spending_score"].idxmin()

print("\nBusiness Insights")

print(
    f"Highest Spending Cluster: {highest_spending}"
)
print("Reason: Customers spend the most.")

print(
    f"Highest Income Cluster: {highest_income}"
)
print("Reason: Customers have the highest income.")

print(
    f"Discount Offers Cluster: {lowest_spending}"
)
print("Reason: Lower spending customers can be attracted with discounts.")

print(
    f"Premium Membership Cluster: {highest_income}"
)
print("Reason: High income customers are ideal for premium membership.")

# -------------------------------
# Question 9
# -------------------------------
joblib.dump(model, "kmeans_model.pkl")

print("\nModel saved as kmeans_model.pkl")