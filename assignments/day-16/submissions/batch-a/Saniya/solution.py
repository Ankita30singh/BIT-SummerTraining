# Day 16 Assignment
#==========================================================>>>
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#==========================================================>>>
# Question 1: Download and Load the Dataset

# Download and load the public dataset:

# ```python
# dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
# df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
# ```

# Print:

# 1. the dataset path;
# 2. the first five rows;
# 3. the DataFrame shape.
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
print(dataset_path)
print("the first five rows")
print(df.head())
print("the DataFrame shape.")
print(df.shape)
print("="*50)
#====================================================================>>>>>
# Question 2: Explore the Dataset

#Print:

    # 1. the column names;
    # 2. each column's data type;
    # 3. descriptive statistics;
    # 4. the missing-value count for every column;
    # 5. the survival counts from `df["Survived"].value_counts()`.

    # In comments, identify the prediction label and state why this is a binary-classification problem.
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())
print(df["Survived"].value_counts())
print("="*50)
#======================================================================>>>>>>
# Question 3: Create an EDA Figure

    # Create one figure containing four subplots:

    # 1. survival counts as a bar chart;
    # 2. average survival rate by `Sex`;
    # 3. average survival rate by `Pclass`;
    # 4. passenger age as a histogram with 20 bins.

    # Give every subplot a title and axis labels. Save the complete figure as:

    # ```text
    # titanic_eda.png
    # ```

    # Use `plt.tight_layout()` and `plt.close()` after saving.


plt.subplot(2,2,1)
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")

plt.subplot(2,2,2)
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Survival by Sex")
plt.xlabel("Sex")
plt.ylabel("Rate")

plt.subplot(2,2,3)
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival by Class")
plt.xlabel("Pclass")
plt.ylabel("Rate")

plt.subplot(2,2,4)
plt.hist(df["Age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()
print("="*50)
#=====================================================================================>>>.
# Question 4: Prepare the Data

    # Create an independent copy with only these columns:

    # ```python
    # data = df[
    #     ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
    # ].copy()
    # ```

    # Then:

    # 1. fill missing `Age` values with the median age;
    # 2. fill missing `Embarked` values with its mode;
    # 3. map `Sex` using `{"male": 0, "female": 1}`;
    # 4. map `Embarked` using `{"S": 0, "C": 1, "Q": 2}`.

    # Print the missing-value counts and data types after preprocessing. The final feature data must contain no missing or text values.
data = df[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked","Survived"]].copy()

data["Age"].fillna(data["Age"].median(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)

data["Sex"] = data["Sex"].map({"male":0,"female":1})
data["Embarked"] = data["Embarked"].map({"S":0,"C":1,"Q":2})

print(data.isnull().sum())
print(data.dtypes)
print("="*50)
#=========================================================================================>>>>
## Question 5: Select Features and Split the Data

    # Create:

    # ```python
    # X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
    # y = data["Survived"]
    # ```

    # Split the data:

    # ```python
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X,
    #     y,
    #     test_size=0.2,
    #     random_state=42,
    #     stratify=y,
    # )
    # ```

    # Print the number of training and testing rows. Explain in a comment why `stratify=y` helps preserve the class proportions.
X = data[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Train:", len(X_train))
print("Test:", len(X_test))                                                             # stratify=y keeps the same class ratio in train and test.
print("="*50)
#===========================================================================>>>>
## Question 6: Train and Evaluate a Decision Tree

    # Train:

    # ```python
    # decision_tree = DecisionTreeClassifier(random_state=42)
    # ```

    # Predict the test data and print:

    # 1. accuracy rounded to three decimal places;
    # 2. the confusion matrix;
    # 3. the classification report.

decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

dt_pred = decision_tree.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, dt_pred),3))
print(confusion_matrix(y_test, dt_pred))
print(classification_report(y_test, dt_pred))
print("="*50)
#=====================================================================================>>>>
## Question 7: Train and Evaluate a Random Forest

#   Train:

    # ```python
    # random_forest = RandomForestClassifier(
    #     n_estimators=100,
    #     random_state=42,
    # )
    # ```

    # Predict the test data and print the same three evaluation results as Question 6.
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest.fit(X_train, y_train)

rf_pred = random_forest.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, rf_pred),3))
print(confusion_matrix(y_test, rf_pred))
print(classification_report(y_test, rf_pred))
print("="*50)
#===========================================================================>>>>>
## Question 8: Compare the Models

    # Create and print a DataFrame with two columns:

    # ```text
    # Model
    # Accuracy
    # ```

    # It must contain one row for the Decision Tree and one for the Random Forest.

    # Plot their accuracies as a bar chart with a y-axis range from `0` to `1`. Save it as:

    # ```text
    # model_accuracy.png
    # ```

    # Print the name of the model with the higher test accuracy. If the accuracies are equal, print that they are tied.
dt_acc = accuracy_score(y_test, dt_pred)
rf_acc = accuracy_score(y_test, rf_pred)

result = pd.DataFrame({
    "Model":["Decision Tree","Random Forest"],
    "Accuracy":[dt_acc, rf_acc]
})

print(result)

plt.bar(result["Model"], result["Accuracy"])
plt.ylim(0,1)
plt.title("Model Accuracy")
plt.savefig("model_accuracy.png")
plt.close()

if dt_acc > rf_acc:
    print("Best Model: Decision Tree")
elif rf_acc > dt_acc:
    print("Best Model: Random Forest")
else:
    print("Both models are tied")

print("="*50)
#=================================================================>>>>>>>
## Question 9: Analyze Feature Importance

    # Create a DataFrame containing each feature and its importance from:

    # ```python
    # random_forest.feature_importances_
    # ```

    # Sort it from highest to lowest and print it.

    # Create a bar chart of the sorted values and save it as:

    # ```text
    # feature_importance.png
    # ```
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_
}).sort_values("Importance", ascending=False)

print(importance)

plt.bar(importance["Feature"], importance["Importance"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()
print("="*50)
#==================================================================>>>>>>
## Question 10: Predict a New Passenger

    # Use:

    # ```python
    # new_passenger = pd.DataFrame({
    #     "Pclass": [3],
    #     "Sex": [0],
    #     "Age": [25],
    #     "SibSp": [1],
    #     "Parch": [0],
    #     "Fare": [8.0],
    #     "Embarked": [0],
    # })
    # ```

    # Use the Random Forest to print:

    # 1. `Survived` or `Not Survived`;
    # 2. the probability of not surviving;
    # 3. the probability of surviving.

    # Round both probabilities to three decimal places. Add a comment explaining that a model probability is an estimate, not a guarantee.
new_passenger = pd.DataFrame({
    "Pclass":[3],
    "Sex":[0],
    "Age":[25],
    "SibSp":[1],
    "Parch":[0],
    "Fare":[8.0],
    "Embarked":[0]
})

pred = random_forest.predict(new_passenger)
prob = random_forest.predict_proba(new_passenger)

print("Prediction:", "Survived" if pred[0]==1 else "Not Survived")
print("Not Survived:", round(prob[0][0],3))
print("Survived:", round(prob[0][1],3))             # Probability is only an estimate, not a guarantee.
print("="*50)
#=========================================================================>>>>>>>>>>>>>>.
