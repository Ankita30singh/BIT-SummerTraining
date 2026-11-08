## Questions 1.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Question 2. 

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd") 

#Question 3.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for num in numbers:
    print(num)  

#Question 4.

def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average

avg = calculate_average(80, 90, 70)
print("Average =", avg) 

#Question 5.
def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# User se marks lena
marks = int(input("Enter marks: "))
grade_student(marks)