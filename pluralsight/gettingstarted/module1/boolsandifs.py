py = True
java = False
print(int(py)) # == 1
print(int(java)) # == 0
print(str(py)) # == "True"

aliens_found = None # undeclared, placeholder

# If statements

number = 5
if number == 5:
    print("number is 5")
else:
    print("number is not 5")

text = "Python" #truthiness: all non zero variables and all non zero size lists are True

if text:
    print(text)

l = [1,2]

if l:
    print("l has stuff")

l = []

if l:
    print("l has stuff")
else:
    print("l is empty")

if number != 6:
    print("number is not 6")

if not py:
    print("not works")

if number == 5 and py:
    print("and")

if number == 6 or py:
    print("or")

a = 1
b = 2
print("bigger") if a > b else print("smaller")
