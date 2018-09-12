students = []


def read_file():
    try:
        with open("students.txt", "r") as f:
            for student in read_student(f):
                students.append(student)
    except Exception:
        print("could not read file")


def read_student(f):
    for line in f:
        yield line


read_file()
print(students)
