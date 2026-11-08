import os

BASE_DIR = os.path.dirname(__file__)

# Question 1: Create and write student.txt
student_path = os.path.join(BASE_DIR, "student.txt")
with open(student_path, "w") as student_file:
    student_file.write("Name: Rohan Nishad\n")
    student_file.write("Age: 20\n")
    student_file.write("College: BIT\n")
print("File created successfully")

# Question 2: Read student.txt and print content
with open(student_path, "r") as student_file:
    content = student_file.read().strip()
print(content)

# Question 3: Append course and city, then read updated file
with open(student_path, "a") as student_file:
    student_file.write("Course: Python Data AI\n")
    student_file.write("City: Gorakhpur\n")
with open(student_path, "r") as student_file:
    updated_content = student_file.read().strip()
print(updated_content)

# Question 4: Count lines in student.txt
with open(student_path, "r") as student_file:
    lines = student_file.readlines()
print(f"Total lines: {len(lines)}")

# Question 5: Write multiple students to students.txt and print names
students_path = os.path.join(BASE_DIR, "students.txt")
students_list = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
with open(students_path, "w") as students_file:
    for student in students_list:
        students_file.write(student + "\n")
with open(students_path, "r") as students_file:
    for line in students_file:
        print(line.strip())

# Question 6: Search a name in students.txt
search_name = input().strip()
with open(students_path, "r") as students_file:
    names = [line.strip() for line in students_file]
print("Found" if search_name in names else "Not Found")

# Question 7: Copy students.txt to students_backup.txt
backup_path = os.path.join(BASE_DIR, "students_backup.txt")
with open(students_path, "r") as source_file:
    with open(backup_path, "w") as backup_file:
        backup_file.write(source_file.read())
print("Backup created successfully")

# Question 8: Create marks.txt and compute total and average
marks_path = os.path.join(BASE_DIR, "marks.txt")
marks_values = [85, 90, 78, 92, 88]
with open(marks_path, "w") as marks_file:
    for mark in marks_values:
        marks_file.write(str(mark) + "\n")
with open(marks_path, "r") as marks_file:
    marks = [int(line.strip()) for line in marks_file]
print(f"Total marks: {sum(marks)}")
print(f"Average marks: {sum(marks) / len(marks)}")
