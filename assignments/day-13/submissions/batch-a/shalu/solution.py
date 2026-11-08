import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Use this student data
student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}
### Question 1: Create and Inspect the DataFrame

"""Create a DataFrame named `df` from `student_data`.

Print:

1. the complete DataFrame;
2. the first five rows;
3. its shape;
4. its descriptive statistics using `describe()`."""
df = pd.DataFrame(student_data)
print(df)
print(df.head(5))
print(df.shape)
print(df.describe())
### Question 2: Select Features and Label

"""Create:

```python
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]
```

Print the first five rows of `X` and `y`.

In a comment, explain why `X` contains features and `y` contains the label."""
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]
print(X.head(5))
print(y.head(5))
# X contains the features as train data to train the model.
# y contains the label the model have to actually predict.

### Question 3: Train a Linear Regression Model

"""Create a `LinearRegression` model and train it using `fit(X, y)`.

Print:

```text
Linear regression model trained
```"""
model = LinearRegression()
model.fit(X,y)
print("Linear regression model trained")

### Question 4: Predict a New Student's Marks

"""Predict the final mark for this student:

```text
study_hours = 6
attendance = 82
previous_mark = 70"""
new_student = pd.DataFrame(
    {
    "study_hours" : [6],
    "attendance" : [82],
    "previous_mark": [70]
    }
)
prediction=model.predict(new_student)
print("Final Marks of student --",round(prediction[0],2))

### Question 5: Inspect Model Coefficients

"""Print the model's coefficients using `model.coef_`.

Add a comment explaining that a coefficient shows how strongly a feature affects the prediction."""
print(model.coef_)
# # A coefficient shows how strongly each feature affects the prediction , Larger cofficient means high prediction

### Question 6: Create and Predict a Pass/Fail Result

"""Create a new column named `result`:

```python
df["result"] = (df["final_marks"] >= 70).astype(int)
```

Here:

- `1` means pass;
- `0` means fail.

Train a `LogisticRegression(max_iter=1000)` model using the same three features and `result` as the label. Predict whether the new student from Question 4 will pass or fail, then print both the number and its meaning."""
df["result"] = (df["final_marks"] >= 70).astype(int)

X_class = df[["study_hours", "attendance", "previous_mark"]]
y_class = df["result"]

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_class, y_class)

result_prediction = log_model.predict(new_student)

print("Prediction (Number):", result_prediction[0])

if result_prediction[0] == 1:
    print("Meaning: Pass")
else:
    print("Meaning: Fail")

### Question 7: Split Training and Testing Data

"""Use:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)
```

Print the number of training rows and testing rows.

In a comment, explain why a model should be tested on data that it did not use for training."""
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
print("Training Rows:", len(X_train))
print("Testing Rows:", len(X_test))
# Model should be tested on new data to test the accuracy of model training, how well the model is trained.

### Question 8: Evaluate the Regression Model

"""Create a new `LinearRegression` model. Train it with `X_train` and `y_train`, then predict `X_test`.

Print:

1. the actual test values;
2. the predicted values;
3. MAE rounded to two decimal places;
4. R² rounded to two decimal places.

Add comments explaining:

- a lower MAE is better;
- an R² value closer to `1` is better."""
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

y_pred = reg_model.predict(X_test)

print(y_test)
print([round(value, 2) for value in y_pred])

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error (MAE):", round(mae, 2))
print("R² Score:", round(r2, 2))
# Lower MAE is better because it means predictions are closer to actual values.
# R² value closer to 1 is better because it indicates the model explains most of the variation in the data.


