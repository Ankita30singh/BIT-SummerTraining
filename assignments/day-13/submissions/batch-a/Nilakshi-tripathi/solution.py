import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}

# Q1: Create and Inspect the DataFrame
df = pd.DataFrame(student_data)

print(df)
print(df.head())
print(df.shape)
print(df.describe())

# Q2: Select Features and Label
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]

print(X.head())
print(y.head())

# X contains input features used for prediction
# y contains target/label we want to predict

# Q3: Train Linear Regression Model
model = LinearRegression()
model.fit(X, y)

print("Linear regression model trained")

# Q4: Predict New Student's Marks
new_student = pd.DataFrame([[6, 82, 70]], columns=X.columns)
prediction = model.predict(new_student)

print(round(prediction[0], 1))

# Q5: Model Coefficients
print(model.coef_)

# Each coefficient shows how strongly a feature affects prediction

# Q6: Pass/Fail using Logistic Regression
df["result"] = (df["final_marks"] >= 70).astype(int)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X, df["result"])

log_pred = log_model.predict(new_student)

print(log_pred[0])
print("1 = Pass, 0 = Fail")

# Q7: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(len(X_train))
print(len(X_test))

# Model should be tested on unseen data to check generalization

# Q8: Evaluate Model
eval_model = LinearRegression()
eval_model.fit(X_train, y_train)

y_pred = eval_model.predict(X_test)

print(y_test.values)
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(round(mae, 2))
print(round(r2, 2))

# Lower MAE is better
# R2 closer to 1 means better performance