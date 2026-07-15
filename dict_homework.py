students = {
    "Abhi" :[90,89,87],
    "Dhanush" :[87,89,96],
    "Prudhu" :[96,97,85],   
    "Thrinaadh" :[89,96,92]
}

subjects = ["Science", "Maths", "Arts"]

for student_1, marks in students.items():
    print(student_1 + ":")
    for student_2, marks_2 in zip(subjects, marks):
         print("  " + student_2 + ":", marks_2)
    total= sum(marks)
    average = total / len(marks)
    print()
    print(" Total", student_1, "marks:", total)
    print(" "+ student_1 + " average marks:", average)
    print(" ")
