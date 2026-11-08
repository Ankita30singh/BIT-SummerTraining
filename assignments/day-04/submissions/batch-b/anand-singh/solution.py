# Question 1: List Append
my_list = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
my_list.append("Vivek")
print(my_list)

# Question 2: Tuple of City Names
cities = ("Gorakhpur", "Varanasi", "Delhi", "Kanpur", "Lucknow")
print(cities[2])  # Accessing the third city in the tuples

# Question 3: Set of Course Names
courses = {"Python", "Java", "C++", "JavaScript"}
courses.add("AI")
print(sorted(courses))

# Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "Batch-2023",
    "city": "Gorakhpur"
}
print("Student Name:", student["name"])
print("Student Course:", student["course"])

# Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.
numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Create a list of words:
# Use a dictionary to count how many times each word appears and print the dictionary.
courses = ["Python", "Java", "C++", "Python", "JavaScript", "Java", "Python"]
word_count = {}
for word in courses:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary.
nested_student = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "data": 90
    },
    "skills": ["Python", "SQL"]
}
nested_student["skills"].append("Pandas")
print(nested_student)

# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = python_students.intersection(ai_students)
print("Common Students:", common_students)