students= {
    "Abhi": [90,80,85],
    "Dhanush": [91,81,86],
    "Prudhu": [92,82,87],
    "Thrinaadh": [93,83,88],
    "Subjects": ["Science", "Arts", "Maths"]
}

"""
Abhi: Science: 90,
      Arts: 80,
      Maths:85,
      
      Total Abhi marks: 225
      Average Abhi marks: 85
"""
for name, marks in students.items():
    if name != "Subjects":
        total = sum(marks)
        average = total / len(marks)

        print(name, students["Subjects"][0], ":", students[name][0])
        print("    ",students["Subjects"][1], ":", students[name][1])
        print("    ",students["Subjects"][2], ":", students[name][2])

        print(name,"total marks:", total)
        print(name,"average marks:", average)
        print("*****************************************")
