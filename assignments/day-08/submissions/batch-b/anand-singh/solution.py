# Question 1: Create a NumPy Array
# Create a one-dimensional NumPy array containing these marks and print it:
import numpy as np
marks = [85, 90, 78, 92, 88]
marks_array = np.array(marks)
print("marks_array:", marks_array)

# Question 2: Array Shape and Size
# Print the shape and total number of elements in the array from Question 1.
import numpy as np
marks = [85, 90, 78, 92, 88]
marks_array = np.array(marks)
print("Shape:", marks_array.shape)
print("Size:", marks_array.size)

# Question 3: Basic Calculations
# Using the marks array, print the total, average, maximum, and minimum.
import numpy as np
marks = [85, 90, 78, 92, 88]
marks_array = np.array(marks)
print("Total:",np.sum(marks_array))
print("Average:",np.mean(marks_array))
print("Maximum:",np.max(marks_array))
print("Minimum:",np.min(marks_array))

# Question 4: Create a 2D Array
# Create this 2D NumPy array and print it:
import numpy as np
array_2d = np.array([[10,20,30],[40,50,60]])
print("array 2d:\n",array_2d)

# Question 5: Indexing and Slicing
# From the 2D array in Question 4, print the value `50` and then print the first row.
print("Value 50:", array_2d[1, 1])
print("First row:", array_2d[0])

# Question 6: Element-Wise Operations
# Create `numbers = np.array([1, 2, 3, 4, 5])`. Print the result of multiplying every element by 10.
import numpy as np
numbers = np.array([1,2,3,4,5])
multiple = numbers * 10
print(multiple)

# Question 7: Filter Values
# Using the marks array, create and print a new array containing marks greater than or equal to 90.
marks = np.array([85, 90, 78, 92, 88])
filtered_marks = marks[marks >= 90]
print("Marks >= 90:", filtered_marks)

# Question 8: Student Marks Matrix
# Create this matrix, where each row represents Python, Data Analytics, and AI marks for one student:
import numpy as mp
mark_matrix = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])
average_mark = np.mean(mark_matrix,axis=1)
print("average marks:",average_mark)