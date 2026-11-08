## Topic: Titanic Classification Project

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

### Question 1: Download and Load the Dataset

dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
print("Dataset Path:")
print(dataset_path)
print("\n First Five Rows:")
print(df.head(5))
print("\n Shape:")
print(df.shape)

print("=" * 50)

### Question 2: Explore the Dataset

print("Column Names:")
print(df.columns.tolist())
print("\n Data Types:")
print(df.dtypes)
print("\n Descriptive Statistics:")
print(df.describe())
print("\n Missing Values:")
print(df.isnull().sum())
print("\n Survival Counts:")
print(df["Survived"].value_counts())

# Prediction Label = Survived
# Binary Classification because output has only two classes:
# 0 = Not Survived
# 1 = Survived

print("=" * 50)

### Question 3: Create an EDA Figure

plt.style.use("dark_background")

fig, ax = plt.subplots(2,2,figsize=(16,11))

fig.patch.set_facecolor("#121212")

fig.suptitle(
    "🚢 TITANIC DATA ANALYTICS DASHBOARD",
    fontsize=24,
    color="white",
    fontweight="bold"
)

# -----------------------------------
# Survival Count
# -----------------------------------

survival=df["Survived"].value_counts().sort_index()

colors=["#ff4d6d","#2ec4b6"]

bars=ax[0,0].bar(
    ["Not Survived","Survived"],
    survival.values,
    color=colors,
    edgecolor="white",
    linewidth=2
)

ax[0,0].set_facecolor("#1f1f1f")
ax[0,0].set_title("Passenger Survival",fontsize=16,fontweight="bold")
ax[0,0].grid(alpha=.3)

for bar in bars:
    ax[0,0].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+5,
        int(bar.get_height()),
        ha="center",
        fontsize=12,
        color="white",
        fontweight="bold"
    )

# -----------------------------------
# Survival by Gender
# -----------------------------------

gender=df.groupby("Sex")["Survived"].mean()*100

bars=ax[0,1].bar(
    gender.index,
    gender.values,
    color=["#00bbf9","#f15bb5"],
    edgecolor="white",
    linewidth=2
)

ax[0,1].set_facecolor("#1f1f1f")
ax[0,1].set_title("Survival Rate by Gender",fontsize=16,fontweight="bold")
ax[0,1].set_ylabel("%")
ax[0,1].grid(alpha=.3)

for b in bars:
    ax[0,1].text(
        b.get_x()+b.get_width()/2,
        b.get_height()+1,
        f"{b.get_height():.1f}%",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# -----------------------------------
# Survival by Class
# -----------------------------------

cls=df.groupby("Pclass")["Survived"].mean()*100

bars=ax[1,0].bar(
    cls.index.astype(str),
    cls.values,
    color=["#ffd166","#06d6a0","#8338ec"],
    edgecolor="white",
    linewidth=2
)

ax[1,0].set_facecolor("#1f1f1f")
ax[1,0].set_title("Passenger Class Survival",fontsize=16,fontweight="bold")
ax[1,0].set_ylabel("%")
ax[1,0].grid(alpha=.3)

for b in bars:
    ax[1,0].text(
        b.get_x()+b.get_width()/2,
        b.get_height()+1,
        f"{b.get_height():.1f}%",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# -----------------------------------
# Age Histogram
# -----------------------------------

n,bins,patches=ax[1,1].hist(
    df["Age"].dropna(),
    bins=20,
    edgecolor="white"
)

gradient=[
"#03045e","#023e8a","#0077b6","#0096c7","#00b4d8",
"#48cae4","#90e0ef","#ade8f4","#caf0f8",
"#ffbe0b","#fb5607","#ff006e",
"#8338ec","#3a86ff","#06d6a0",
"#f15bb5","#9b5de5","#00f5d4",
"#ff9f1c","#2ec4b6"
]

for p,c in zip(patches,gradient):
    p.set_facecolor(c)

median=df["Age"].median()

ax[1,1].axvline(
    median,
    color="red",
    linewidth=3,
    linestyle="--",
    label=f"Median {median:.1f}"
)

ax[1,1].legend()

ax[1,1].set_facecolor("#1f1f1f")
ax[1,1].set_title("Passenger Age Distribution",fontsize=16,fontweight="bold")
ax[1,1].grid(alpha=.3)

plt.tight_layout()

plt.savefig(
    "titanic_eda.png",
    dpi=350,
    bbox_inches="tight"
)

plt.close()
print("="*50)

### Question 4: Prepare the Data

data = df[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
        "Survived",
    ]
].copy()

data["Age"].fillna(data["Age"].median(), inplace=True)

data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)

data["Sex"] = data["Sex"].map(
    {
        "male":0,
        "female":1
    }
)

data["Embarked"] = data["Embarked"].map(
    {
        "S":0,
        "C":1,
        "Q":2
    }
)

print("Missing Values After Preprocessing")
print(data.isnull().sum())
print("Data Types After Preprocessing")
print(data.dtypes)

print("=" * 50)

### Question 5: Select Features and Split the Data

X = data[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
    ]
]

y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("Training Rows :", len(X_train))
print("Testing Rows :", len(X_test))

# stratify=y keeps survival ratio almost same in train and test data

print("=" * 50)

### Question 6: Train and Evaluate a Decision Tree

decision_tree = DecisionTreeClassifier(random_state=42)

decision_tree.fit(X_train,y_train)

dt_prediction = decision_tree.predict(X_test)

dt_accuracy = accuracy_score(y_test,dt_prediction)

print("Decision Tree Accuracy :",round(dt_accuracy,3))

print()

print("Decision Tree Confusion Matrix:")
print(confusion_matrix(y_test,dt_prediction))

print()

print("Decision Tree Classification Report:")
print(classification_report(y_test,dt_prediction))

print("=" * 50)

### Question 7: Train and Evaluate a Random Forest

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest.fit(X_train,y_train)

rf_prediction = random_forest.predict(X_test)

rf_accuracy = accuracy_score(y_test,rf_prediction)

print("Random Forest Accuracy :",round(rf_accuracy,3))

print()

print("Random Forest Confusion Matrix:")
print(confusion_matrix(y_test,rf_prediction))

print()

print("Random Forest Classification Report:")
print(classification_report(y_test,rf_prediction))

print("=" * 50)

### Question 8: Compare the Models

result = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [dt_accuracy, rf_accuracy]
})

plt.style.use("dark_background")

plt.figure(figsize=(9,6))

colors=["#ff006e","#3a86ff"]

bars=plt.bar(
    result["Model"],
    result["Accuracy"],
    color=colors,
    edgecolor="white",
    linewidth=2
)

plt.title(
    "MODEL ACCURACY COMPARISON",
    fontsize=20,
    fontweight="bold"
)

plt.ylim(.6,1)

plt.grid(alpha=.3)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+0.005,
        f"{bar.get_height():.3f}",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

plt.savefig(
    "model_accuracy.png",
    dpi=350,
    bbox_inches="tight"
)

plt.close()

print("=" * 50)

### Question 9: Analyze Feature Importance

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_
})
importance = importance.sort_values(
    by="Importance",
    ascending=True
)

plt.style.use("dark_background")

plt.figure(figsize=(11,7))

colors=[
"#8338ec",
"#ff006e",
"#fb5607",
"#ffbe0b",
"#06d6a0",
"#00bbf9",
"#3a86ff"
]

bars=plt.barh(
    importance["Feature"],
    importance["Importance"],
    color=colors,
    edgecolor="white",
    linewidth=2
)

plt.title(
    "RANDOM FOREST FEATURE IMPORTANCE",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Importance Score")

plt.grid(alpha=.3)

for bar in bars:
    plt.text(
        bar.get_width()+0.003,
        bar.get_y()+bar.get_height()/2,
        f"{bar.get_width():.3f}",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

plt.savefig(
    "feature_importance.png",
    dpi=350,
    bbox_inches="tight"
)

plt.close()

print("=" * 50)

### Question 10: Predict a New Passenger

new_passenger = pd.DataFrame(
    {
        "Pclass" : [3],
        "Sex" : [0],
        "Age" : [25],
        "SibSp" : [1],
        "Parch" : [0],
        "Fare" : [8.0],
        "Embarked":[0],
    }
)

prediction = random_forest.predict(new_passenger)

probability = random_forest.predict_proba(new_passenger)

if prediction[0] == 1:
    print("Prediction : Survived")
else:
    print("Prediction : Not Survived")

print("Probability of Not Survived :", round(probability[0][0],3))
print("Probability of Survived :", round(probability[0][1],3))

# Probability is only a prediction estimate.
# It is not a guarantee.

print("=" * 50)
