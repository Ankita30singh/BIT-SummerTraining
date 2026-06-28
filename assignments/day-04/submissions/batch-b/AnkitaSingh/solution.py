# create a list of 5 students names . Add one new student name to the list and print the final list

stu_names=['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh']
stu_names.append("Vivek")
print(stu_names)

# create a tuple of 5 city names and print the third city
tpl = ("Varanasi","Haridwar","Delhi","Kanpur","Delhi")
print(tpl[2])

# create a set of 4 course names. add "AI" to the set and print the sorted list of courses
courses = {'Data Analytics', 'Machine Learning', 'Python', 'SQL'}
courses.add("AI")
sorted_courses = sorted(courses)
print( sorted_courses)

#Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.
dict1 = {"Name":"Rahul", "Course":"Python Data AI","Batch":"B","City":"Deoria"}
print("Name:", dict1["Name"])
print("Course:", dict1["Course"])

#Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it
lst1 = [1,2,3,4,5,6,7,8,9,10]
even = []
for i in lst1:
    if i%2 == 0:
        even.append(i)
    i += 1
print(even)


#  Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]
dict1 = {}
count = 0

for i in words:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)


#Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary.
dict2 = {'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL']}
dict2["skills"].append("Pandas")
print(dict2)


# create 2 sets and Find the common students and print them as a sorted list.
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = set()
for i in python_students:
    for j in ai_students:
        if i == j:
            common_students.add(i)
        
print(sorted(common_students))