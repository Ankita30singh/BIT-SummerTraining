#assignment 11

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Use this data to create a DataFrame:

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}

# Question 1: Set a Theme
# Set a Seaborn theme using sns.set_theme(style="whitegrid") before creating charts.

sns.set_theme(style="whitegrid")
df = pd.DataFrame(student_data)
print(df)


# Question 2: Count Plot
# Create a count plot showing the number of students in each course.
# Title: Students by Course
# Save as course_count.png

plt.figure(figsize=(6,4))
sns.countplot(x="course", data=df, palette="Set2")
plt.title("Students by Course")
plt.savefig("course_count.png")
plt.close()
plt.close()


# Question 3: Bar Plot
# Create a bar plot showing the average marks for each course.
# Title: Average Marks by Course
# Save as average_marks_bar.png

plt.figure(figsize=(6,4))
sns.barplot(x="course", y="marks", data=df, estimator="mean", palette="Set2")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.close()
plt.close()


# Question 4: Scatter Plot
# Create a scatter plot showing study_hours on the x-axis and marks on the y-axis. Use course as the color grouping.
# Title: Study Hours vs Marks
# Save as study_hours_marks_scatter.png

plt.figure(figsize=(6,4))
sns.scatterplot(x="study_hours", y="marks", hue="course", data=df, palette="Set2", s=100)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.close()
plt.close()

# Question 5: Box Plot
# Create a box plot of marks grouped by course.
# Title: Marks Distribution by Course
# Save as marks_boxplot.png

plt.figure(figsize=(6,4))
sns.boxplot(x="course", y="marks", data=df, palette="Set2")
plt.title("Marks Distribution by Course")
plt.xlabel("Course")
plt.ylabel("Marks")
plt.savefig("marks_boxplot.png")
plt.close()
plt.close()


# Question 6: Histogram
# Create a histogram of marks with a KDE curve.
# Title: Marks Distribution
# Save as marks_histogram.png

plt.figure(figsize=(6,4))
sns.histplot(df["marks"], kde=True, color="skyblue", palette="Set2")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.savefig("marks_histogram.png")
plt.close()
plt.close()



# Question 7: Correlation Heatmap
# Create a correlation heatmap for study_hours, marks, and attendance.
# Use annot=True
# Title: Student Metrics Correlation
# Save as student_correlation_heatmap.png

correlation = df[["study_hours", "marks", "attendance"]].corr()
plt.figure(figsize=(6,4))
sns.heatmap(correlation, annot=True, cmap="Blues", fmt=".2f")
plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.close()
plt.close()



# Question 8: Best Performing Course
# Use Pandas groupby to find the course with the highest average marks and print it.
# Expected Output:
# Best performing course: AI


avg_marks = df.groupby("course")["marks"].mean()
best_course = avg_marks.idxmax()
print(f"Best performing course: {best_course}")


