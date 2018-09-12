students = []


class Student:

    school_name = "Springfield elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalize(self):
        return super().get_name_capitalize() + " HS"


# james = HighSchoolStudent("james")

# print(james.get_name_capitalize())
# print(james.get_school_name())

# mark = Student("Mark")
# print(mark)

# print(Student.school_name)
