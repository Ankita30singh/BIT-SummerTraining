# 1. Create a list of 5 student names and print all names.
student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]
print("Student names:", student_names)

# 2. Add one new student name to the list.
student_names =["anand", "sachin", "rohit", "rahul", "saurabh"]
print("student names:", student_names)
student_names.append("alok")
print("new student names:", student_names)

    
# 3. Create a tuple of 5 city names and print the second city.
city_names = ("gurgaon", "delhi", "mumbai", "bangalore", "kolkata")
print("second city:", city_names[1])

# 4. Create a set of 5 course names and add one new course.
course_names = {"python", "java", "c++", "javascript", "html"}
print("Course names:", course_names)
course_names.add("css")
print("Updated course names:", course_names)

# 5. Create a dictionary for one student with name, branch, batch, and marks.
dict_student = {
    "name": "Anand Singh",
    "branch": "Computer Science",
    "batch": "Batch B",
    "marks": 85
}
print("Student Dictionary:", dict_student)

# 6. Print the student dictionary in a readable format.
dict_student = {
    "name": "Anand Singh",
    "branch": "Computer Science",
    "batch": "Batch B",
    "marks": 85
}
print("\nStudent Dictionary in Readable Format:")
for key, value in dict_student.items():
    print(f"{key.capitalize()}: {value}")
    