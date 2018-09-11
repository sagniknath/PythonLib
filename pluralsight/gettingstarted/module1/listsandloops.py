student_names = ['mark', 'katrina', 'jessica']
print(student_names)
print(student_names[0])
print(student_names[-1])
student_names[0] = "James"
print(student_names)
student_names.append("Chad")
print(student_names)
if 'James' in student_names:
    print('James is in')

print(len(student_names))
del student_names[2]
print(student_names)

print(student_names[1:])  # slicing
print(student_names[1:-1])

for name in student_names:
    print(f"Student name is {name}")

for index in range(10):
    print("x is {0}".format(index * 10))
print("")
for index in range(5, 10):
    print("x is {0}".format(index * 10))
print("")

for index in range(5, 10, 2):
    print("x is {0}".format(index * 10))

for name in student_names:
    print(name)
    if name is "James":
        print("found it")
        break              #continue

x = 0
while x < 10:
    print(f"x is {x}")
    x += 1





