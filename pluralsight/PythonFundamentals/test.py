import math
from math import factorial as fact

print(math.sqrt(4))

# help(math)
# help(math.factorial)

print(math.factorial(5))

print(fact(5)//fact(2) * fact(3))

print(fact(100))

print(0b10)
print(0o10)
print(0x10)
print(int("10000", 3))

print(3e8)

print(1.616e-35)

print(float("nan"))
print(float("-inf"))

x = """This is 
a 
multiline string"""

print(x)

path = r'C:\users\snath'
print(path)

print(type(x[4]))

c = 'oslo'
print(c.capitalize())

x = b'some data'
print(x)
print(x.split())

from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

print(story_words)