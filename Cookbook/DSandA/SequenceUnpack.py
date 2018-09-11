# Problem 1.1: You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

# Any sequence (or iterable) can be unpacked into variables using a simple assignment
# operation. The only requirement is that the number of variables and structure match
# the sequence.

p = (4, 5)
x, y = p
print(f"{x} {y}")

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data

print(name)
print(day)

# If there is a mismatch in the number of elements, you’ll get an error.

try:
    p = (4, 5)
    x, y, z = p
except ValueError as error:
    print(error)

# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.

s = 'Hello'
a, b, c, d, e = s
print(a)

# When unpacking, you may sometimes want to discard certain values. Python has no
# special syntax for this, but you can often just pick a throwaway variable name for it.

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)

# Problem 1.2: You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a “too many values to unpack” exception

# Python “star expressions” can be used to address this problem. For example, suppose
# you run a course and decide at the end of the semester that you’re going to drop the first
# and last homework grades, and only average the rest of them. If there are only four
# assignments, maybe you simply unpack all four, but what if there are 24? A star expression
# makes it easy:


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)

# It’s worth noting that the phone_numbers variable will always be a list, regardless of how
# many phone numbers are unpacked (including none). Thus, any code that uses
# phone_numbers won’t have to account for the possibility that it might not be a list or
# perform any kind of additional type checking.

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x1, y1):
    print('foo', x1, y1)


def do_bar(s1):
    print('bar', s1)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Star unpacking can also be useful when combined with certain kinds of string processing
# operations, such as splitting.

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

# Sometimes you might want to unpack values and throw them away. You can’t just specify
# a bare * when unpacking, but you could use a common throwaway variable name, such
# as _ or ign (ignored).

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# There is a certain similarity between star unpacking and list-processing features of various
# functional languages. For example, if you have a list, you can easily split it into head
# and tail components

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(tail)


def sum2(items2):
    head, *tail = items2
    return head + sum(tail) if tail else head

print(sum2(items))