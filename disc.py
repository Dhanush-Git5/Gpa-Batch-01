student = { "name" : "Dhanush",
            "age" : 13,
            "grade" : 8 
}

print(student)
print(student["grade"])

student["school"] = "vickery creek middle school"

print(student)

for key, value in student.items():
    print(key, ": ", value)