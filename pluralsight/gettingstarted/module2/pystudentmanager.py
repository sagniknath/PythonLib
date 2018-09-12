students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].strip().title())
    return students_titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        with open("students.txt", "a") as f:
            f.write(student + "\n")
    except Exception:
        print("Unable to save file")


def read_file():
    try:
        with open("students.txt", "r") as f:
            for student in f.readlines():
                add_student(student)
    except Exception:
        print("could not read file")


read_file()

print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)

save_file(student_name)
