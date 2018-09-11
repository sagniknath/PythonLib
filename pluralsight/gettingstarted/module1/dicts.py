student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

print(student['name'])
print(student.get("last_name", "unknown"))
print(student.keys())
print(student.values())
try:
    print(student['last_name'])
except KeyError:
    print("Error finding last name")

student["last_name"] = "Judd"
try:
    print(student['last_name'] + 3)
except KeyError:
    print("Error finding last name")
except TypeError as error:
    print("Cant add these")
    print(error)
# except Exception:
#    print("Unknown error")

print("This code executes")
