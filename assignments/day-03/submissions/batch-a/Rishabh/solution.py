# Question 1: Create a list of 5 student names and print all names

students = ["Rishabh", "Aman", "Ansh", "Saniya", "Vivek"]

print("Student Names:")
for student in students:
    print(student)

# Question 2: Add one new student name to the list

students.append("Muskan")

print("\nUpdated Student List:")
print(students)

# Question 3: Create a tuple of 5 city names and print the second city

cities = ("Lucknow", "Kanpur", "Delhi", "Mumbai", "Pune")

print("\nSecond City:")
print(cities[1])

# Question 4: Create a set of 5 course names and add one new course

courses = {"Python", "Java", "C++", "HTML", "CSS"}

courses.add("JavaScript")

print("\nCourses:")
print(courses)

# Question 5: Create a dictionary for one student

student = {
    "name": "Rishabh Bhaskar Shahi",
    "branch": "CSE",
    "batch": "A",
    "marks": 85
}

# Question 6: Print dictionary in readable format

print("\nStudent Details:")
print("Name:", student["name"])
print("Branch:", student["branch"])
print("Batch:", student["batch"])
print("Marks:", student["marks"])