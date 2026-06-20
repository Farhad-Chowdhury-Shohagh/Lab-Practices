student = {
    "name": "Farhad Chowdhury",
    "age": 22,
    "home": "Dhaka"
}
academicInfo = {
    "university": "Eastern University",
    "id": 232400025,
    "department": "CSE",
    "semester": "10th",
    "cgpa": 3.79
}

print("Original Dictionary: ")
print(student)

#get()
print("Student Name: ", student.get("name"))
print("Student CGPA: ", student.get("cgpa"))

#keys()
print("All Keys: ", student.keys())

#values()
print("All Values: ", student.values())

#items()
print("All Items: ", student.items())

#update(dict)
student.update(academicInfo)
print("After Update:", student)

#pop(key)
student.pop("semester")
print("After pop:", student)

#popitem()
student.popitem()
print("After popitem:", student)

#copy()
studentInfo = student.copy()
print("Copied Dictionary:", studentInfo)

#setdefault(key, default)
student.setdefault("phone", "Not Provided")
print("After setdefault:", student)

#clear()
student.clear()
print("After clear:", student)
