# strings are ascii by default in py2 and unicode by default in py3
""" doc comments """

print(dir(""))
print("hello".capitalize())
print("hello".replace('e','a'))
print("hello".isalpha())
print("123".isdigit())
print("some,csv,values".split(","))

name = "pythonBo"
machine = "HAL"

print("Nice to meet you {0}, I am {1}".format(name, machine))
print(f"Nice to meet you {name}, I am {machine}")
