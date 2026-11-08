# Day 8

import numpy as np

# Question 1: Create a NumPy Array
# Expected Output:
# [85 90 78 92 88]
marks = np.array([85, 90, 78, 92, 88])
print(marks)
print()


# Question 2: Array Shape and Size
# Expected Output:
# Shape: (5,)
# Size: 5
print("Shape:", marks.shape)
print("Size:", marks.size)
print()


# Question 3: Basic Calculations
# Expected Output:
# Total: 433
# Average: 86.6
# Maximum: 92
# Minimum: 78
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print()


# Question 4: Create a 2D Array
# Expected Output:
# [[10 20 30]
#  [40 50 60]]
array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(array_2d)
print()

# Question 5: Indexing and Slicing
# Expected Output:
# 50
# [10 20 30]
print(array_2d[1][1])
print(array_2d[0])
print()


# Question 6: Element-Wise Operations
# Expected Output:
# [10 20 30 40 50]
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)
print()


# Question 7: Filter Values
# Expected Output:
# [90 92]
print(marks[marks >= 90])
print()


# Question 8: Student Marks Matrix
# Expected Output:
# [84.33 91.67 79.33]
student_marks = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])
average_marks = np.round(student_marks.mean(axis=1), 2)
print(average_marks)
