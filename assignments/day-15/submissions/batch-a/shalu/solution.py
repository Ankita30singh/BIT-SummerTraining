import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
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

### Question 1: Load and Inspect the Data

"""Create a DataFrame named `df` from `customer_data`.

Print:

1. the first five rows;
2. the DataFrame shape;
3. the column names;
4. the missing-value count for each column."""
df = pd.DataFrame(customer_data)
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
### Question 2: Select the Clustering Features
"""Create:

```python
X = df[["annual_income", "spending_score"]]
```

Print the first five rows of `X`.

In a comment, explain why `customer_id` should not be used as a clustering feature."""
X = df[["annual_income", "spending_score"]]
print(X.head())
# customer_id should not be used for clustring feature because it is only a unique identifier and does not describe customer behaviour or purchasing patterns.

### Question 3: Use the Elbow Method

"""For every value of `k` from `1` to `7`:

1. create `KMeans(n_clusters=k, random_state=42, n_init=10)`;
2. train it with `X`;
3. add its `inertia_` value to a list named `inertias`.

Print each `k` and inertia value rounded to two decimal places.

Plot the inertia values against `k` using markers, axis labels, a title, and a grid. Save the chart as:

```text
elbow_curve.png
```

Use `plt.tight_layout()` and `plt.close()` after saving."""
inertias = []

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
### Question 4: Train the Final K-Means Model

"""Use three clusters:

```python
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)
```

Print the complete DataFrame and the number of customers in each cluster.

Add a comment explaining why cluster numbers such as `0`, `1`, and `2` are identifiers rather than rankings."""
model = KMeans(n_clusters=3, random_state=42, n_init=10)

df["cluster"] = model.fit_predict(X)

print(df)
print(df["cluster"].value_counts().sort_index())
# Cluster labels (0, 1, 2) are only identifiers assigned by the algorithm.They do not represent rankings or any order of importance.

### Question 5: Inspect the Centroids

"""Get the cluster centres using:

```python
centroids = model.cluster_centers_
```

Print the centroids rounded to two decimal places. Clearly label the income and spending values in your output."""
centroids = model.cluster_centers_

for i, center in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Annual Income = {center[0]:.2f}, "
        f"Spending Score = {center[1]:.2f}"
    )

### Question 6: Visualize Clusters and Centroids

"""Create a scatter plot with:

- annual income on the x-axis;
- spending score on the y-axis;
- customer points coloured by cluster;
- centroids shown as large red `X` markers;
- a title, axis labels, colour bar, and centroid legend.

Save it as:

```text
customer_clusters.png
```

Use `plt.tight_layout()` and `plt.close()` after saving."""
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

### Question 7: Calculate the Silhouette Score

"""Calculate:

```python
score = silhouette_score(X, df["cluster"])
```

Print the score rounded to three decimal places.

In a comment, explain that a higher silhouette score generally means points are closer to their own cluster and farther from other clusters."""
score = silhouette_score(X, df["cluster"])
print(f"Silhouette Score: {score:.3f}")
# A higher silhouette score generally indicates that points are closer to their own cluster and farther from other clusters.

### Question 8: Produce Business Insights

"""Group the DataFrame by `cluster` and calculate the average annual income and spending score for each cluster.

Print the summary table, then identify:

1. the cluster with the highest average spending score;
2. the cluster with the highest average income;
3. a cluster that could receive discount offers;
4. a cluster that could receive premium-membership offers.

Print one short reason for each marketing choice. Derive the cluster numbers from the summary instead of assuming a fixed label."""
summary = (
    df.groupby("cluster")[["annual_income", "spending_score"]]
    .mean()
    .round(2)
)

print(summary)

highest_spending_cluster = summary["spending_score"].idxmax()
highest_income_cluster = summary["annual_income"].idxmax()
discount_cluster = summary["spending_score"].idxmin()
premium_cluster = highest_spending_cluster

print(f"Cluster with highest average spending score: {highest_spending_cluster}")
print("Reason: Customers spend the most and are highly engaged.")

print(f"Cluster with highest average income: {highest_income_cluster}")
print("Reason: Customers have the greatest purchasing power.")

print(f"Cluster for discount offers: {discount_cluster}")
print("Reason: Lower spending customers may be encouraged with discounts.")

print(f"Cluster for premium membership offers: {premium_cluster}")
print("Reason: High spending customers are ideal for premium services.")

### Question 9: Export the Model

"""Save the trained model:

```python
joblib.dump(model, "kmeans_model.pkl")
```

Print:

```text
Model saved as kmeans_model.pkl
```"""
joblib.dump(model, "kmeans_model.pkl")
print("Model saved as kmeans_model.pkl")