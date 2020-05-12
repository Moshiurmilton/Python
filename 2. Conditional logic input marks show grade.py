marks= input("Please enter your marks: ")
marks = int(marks)
if marks >= 80:
    grade = "A+"
    print("Your grade is", grade)
elif marks>= 70:
    grade = "A"
    print("Your grade is", grade)
elif marks >= 60:
    grade = "A-"
    print("Your grade is", grade)
elif marks >= 50:
    grade = "B"
    print("Your grade is", grade)
elif marks >= 40:
    grade = "C"
    print("Your grade is", grade)
else:
    grade = "F"
    print("Your grade is", grade)
