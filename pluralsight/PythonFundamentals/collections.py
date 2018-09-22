h = (391)
print(type(h))

h = (391,)
print(type(h))

e = ()
print(type(e))

print(''.join(["Adsfa", "asdfa", "SDFa"]))

prefix, _, suffix = "unforgettable".partition("forget")
print(prefix, suffix)

print("The age of {0} is {1}".format("Mark", 21))

s = "Current position {long} {lat}".format(long=123, lat=232)
print(s)

pos1 = (42.1, 423.4, 631.4)
print("Galactic position {pos[0]} {pos[1]} {pos[2]}".format(pos=pos1))

import math

print("Math constants: pi={m.pi} e={m.e}".format(m=math))

t = [1, 3, 51, 234]
for p in enumerate(t):
    print(p)

for a, b in enumerate(t):
    print(a, b)

s = [1, 2, 3, 4, 5]

print(s[:2])
print(s[:2] + s[2:])
print(s[:])

# shallow copy idioms
full_slice = s[:]
print(full_slice is s)
print(full_slice[0] is s[0])
print(id(full_slice[0]), id(s[0]))

u = s.copy()
v = list(s)

c = [21, 37]
d = c * 5
print(d)
print(d[0] is d[2])

# search
print(s.index(5))
print(5 in s)
print(6 not in s)
print(s.count(1))
try:
    print(s.index('ads'))
except ValueError:
    print('ads not found')

# insert and delete
del s[3]
print(s)
s.remove(5)
print(s)
s.insert(4, 5)
print(s)
s += [1, 2]
s.extend([1, 2])
print(s)

# reverse and sort
s.reverse()
print(s)
s.sort()
print(s)
s.sort(reverse=True)
print(s)
s.sort(reverse=True, key=lambda x: -x)
print(s)

x = reversed(s)
y = sorted(s)
print(list(x), y)
