student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades={}

# TODO-2: Write your code below to add the grades to student_grades.👇
for item in student_scores:
    if student_scores[item]>=91:
        student_grades[item]="Outstanding"
    elif student_scores[item]>=81:
        student_grades[item]="Exceeds Expectations"
    elif student_scores[item]>=71:
        student_grades[item]="Acceptable"
    else:
        student_grades[item]="Fail"

# 🚨 Don't change the code below 👇
print(student_grades)





