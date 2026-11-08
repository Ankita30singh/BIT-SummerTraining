# Day 14 Assignment

## Topic: Unsupervised Learning and K-Means Fundamentals

Complete all questions in one file named `solution.py`.

Use NumPy for the calculations. This assignment performs the K-means steps manually so that you understand how centroids and distances work.

Install NumPy if required:

```bash
python3 -m pip install numpy
```

Start your program with:

```python
import numpy as np
```

Use this customer data:

```python
# Each row contains: [annual_income, spending_score]
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])
```

## Questions

### Question 1: Understand the Data

Print the customer array, its shape, and the total number of customers.

In a comment, explain why this is an unsupervised-learning problem when no customer group labels are supplied.

### Question 2: Calculate a Centroid

Use this group:

```python
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])
```

Calculate its centroid using the mean of each column. Print the centroid.

Expected value:

```text
[30. 40.]
```

### Question 3: Initial Centroids and Customer P

Create:

```python
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])
```

Print all three arrays.

### Question 4: Euclidean Distance Function

Write this function:

```python
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))
```

Use it to calculate the distance from `customer_p` to `centroid_a` and `centroid_b`. Print both distances rounded to two decimal places.

### Question 5: Assign Customer P

Compare the two distances from Question 4.

Print:

```text
Customer P belongs to Cluster A
```

or:

```text
Customer P belongs to Cluster B
```

Use an `if` statement instead of writing the answer directly.

### Question 6: Assign Every Customer

For every row in `customers`:

1. calculate its distance from `centroid_a`;
2. calculate its distance from `centroid_b`;
3. add it to `cluster_a` or `cluster_b`, depending on the smaller distance.

Convert both cluster lists to NumPy arrays and print them.

### Question 7: Recalculate the Centroids

Calculate and print the new centroid of `cluster_a` and `cluster_b` using:

```python
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)
```

Print each new centroid rounded to two decimal places.

### Question 8: Explain the K-Means Cycle

At the bottom of `solution.py`, add comments explaining these steps in your own words:

```text
Find the nearest centroid
Assign points to groups
Calculate each group's new average
Move the centroids
Repeat until the groups stop changing
```

Also print one sentence explaining why the algorithm may need several rounds.

## Submission

Create your solution here:

```text
assignments/day-14/submissions/batch-a/your-name/solution.py
```

or:

```text
assignments/day-14/submissions/batch-b/your-name/solution.py
```

Run your program before submitting:

```bash
python3 assignments/day-14/submissions/batch-a/your-name/solution.py
```
