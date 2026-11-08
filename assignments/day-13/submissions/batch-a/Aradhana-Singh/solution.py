import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Use this student data:
student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}

# ### Question 1: Create and Inspect the DataFrame
# Create a DataFrame named `df` from `student_data`.
df = pd.DataFrame(student_data)
# Print:
# 1. the complete DataFrame;
print(df)
# 2. the first five rows;
print(df.head(5))
# 3. its shape;
print(df.shape)
# 4. its descriptive statistics using `describe()`.
print(df.describe())


# ### Question 2: Select Features and Label
# Create:
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]


# Print the first five rows of `X` and `y`.
print(X.head(5))
print(y.head())
# In a comment, explain why `X` contains features and `y` contains the label.
# X contains the input features used to make predictions.
# y contains the target (label) that the model learns to predict.


# ### Question 3: Train a Linear Regression Model
# Create a `LinearRegression` model and train it using `fit(X, y)`.
model = LinearRegression()
model.fit(X, y)
# Print:
# Linear regression model trained
print("Linear regression model trained")

# ### Question 4: Predict a New Student's Marks
# Predict the final mark for this student:
# study_hours = 6
# attendance = 82
# previous_mark = 70
# Create the new student as a one-row DataFrame with the same feature column names as `X`. Print the predicted mark rounded to one decimal place.
new_student = pd.DataFrame({
    "study_hours":[6],
    "attendance":[82],
    "previous_mark":[70]
})
predicted = model.predict(new_student)
print("Predicted Marks:", round(predicted[0],1))


# ### Question 5: Inspect Model Coefficients
# Print the model's coefficients using `model.coef_`.
print("Model Coefficients:", model.coef_)

# Add a comment explaining that a coefficient shows how strongly a feature affects the prediction.
# A coefficient shows how strongly a feature affects the prediction.


# ### Question 6: Create and Predict a Pass/Fail Result
# Create a new column named `result`:
df["result"] = (df["final_marks"] >= 70).astype(int)

# Here:
# - `1` means pass;
# - `0` means fail.
# Train a `LogisticRegression(max_iter=1000)` model using the same three features and `result` as the label. Predict whether the new student from Question 4 will pass or fail, then print both the number and its meaning.
X = df[["study_hours", "attendance", "previous_mark"]]
y_result = df["result"]
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X, y_result)
prediction = log_model.predict(new_student)
print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Meaning: Pass")
else:
    print("Meaning: Fail")


# ### Question 7: Split Training and Testing Data
# Use:
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)
# Print the number of training rows and testing rows.
print("Training Rows:", X_train.shape[0])
print("Testing Rows:", X_test.shape[0])
# In a comment, explain why a model should be tested on data that it did not use for training.
# Testing on unseen data helps measure the model's real performance.


# ### Question 8: Evaluate the Regression Model
# Create a new `LinearRegression` model. Train it with `X_train` and `y_train`, then predict `X_test`.
new_model = LinearRegression()
new_model.fit(X_train, y_train)
y_pred = new_model.predict(X_test)
# Print:
# 1. the actual test values;
print("Actual Test Values:", y_test.values)

# 2. the predicted values;
print("Predicted Values:", y_pred)

# 3. MAE rounded to two decimal places;
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error (MAE):", round(mae, 2))

# 4. R² rounded to two decimal places.
r2 = r2_score(y_test, y_pred)
print("R² Score:", round(r2, 2))

# Add comments explaining:
# - a lower MAE is better;
# A lower MAE means the prediction error is smaller, so the model is better.

# - an R² value closer to `1` is better.
# An R² value closer to 1 means the model predicts the data more accurately.