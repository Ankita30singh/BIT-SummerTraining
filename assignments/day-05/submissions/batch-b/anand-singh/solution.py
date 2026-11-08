# Question 1: Create and Write a File
with open("student.txt", "w") as f:
    f.write("Name: Rahul\n")
    f.write("Age: 20\n")
    f.write("College: BIT\n")
print("File created successfully.")

# Question 2: Read a File
with open("student.txt", "r") as f:
    content = f.read()
print(content)

# Question 3: Append to a File
with open("student.txt", "a") as f:
    f.write("Course: Python Data AI\n")
    f.write("City: Gorakhpur\n")
with open("student.txt", "r") as f:
    content = f.read()
print(content)

# Question 4: Count Lines in a File
with open("student.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))

# Question 5: Write Multiple Students

with open("students.txt", "w") as f:
    f.write("Aman\n")
    f.write("Priya\n")
    f.write("Shalu\n")
    f.write("Raj\n")
    f.write("Ansh\n")

with open("students.txt", "r") as f:
    names = f.readlines()
    for name in names:
        print(name.strip())

# Question 6: Search a Name in File  
with open("students.txt", "r") as f:
    names = f.readlines()
    search_name = input("Enter a student name: ").strip()
    if search_name +"\n" in names:
        print("Found")
    else:
        print("Not Found")

# Question 7: Copy File Content
with open("students.txt", "r") as source_file:
    content = source_file.read()
with open("students_backup.txt", "w") as backup_file:
    backup_file.write(content)
print("Backup created successfully.")

# Question 8: Marks File Summary
with open("marks.txt", "w") as f:
    f.write("Rahul: 85\n")
    f.write("Aman: 90\n")
    f.write("Priya: 78\n")
    f.write("Shalu: 92\n")
    f.write("Raj: 88\n")
    f.close()
Total_marks = 0
with open("marks.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        name, marks = line.strip().split(": ")
        Total_marks += int(marks)
Average_marks = Total_marks / len(lines)
print(f"Total marks: {Total_marks}")
print(f"Average marks: {Average_marks:.2f}")