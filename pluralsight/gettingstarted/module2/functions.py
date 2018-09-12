students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student['name'].title()
    return students_titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def var_args(name, *args):
    print(name)
    print(args)


def var_args2(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs['subs'])


add_student(name="mark stuart", student_id=15)


print_students_titlecase()

var_args("mark", "loves", "python", True, 0, None)

var_args2("Mark", description="Loves Python", feedback=None, subs=True)

