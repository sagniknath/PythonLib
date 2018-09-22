words = ["adsa", "awerr", "bfgfg"]
print([letter for word in words for letter in word if letter < 'h'])
print({letter for word in words for letter in word if letter < 'h'})

d = dict(a=1, b=2, c=3)
print(d)
d_invert = {num: let for let, num in d.items()}
print(d_invert)

# iteration protocols

iterable = ["Summer", "Spring", "Autumn", "Winter"]
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    pass


def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
print(g)

print(next(g))
print(next(g))
print(next(g))

try:
    print(next(g))
except StopIteration:
    pass

for v in gen123():
    print(v)

# generator comprehension
for v in (x for x in range(1, 10)):
    print(v)


from itertools import islice, count


def is_prime(num):
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

print(sum(thousand_primes))


print(any([True, False, False]))

print(all([True, False, False]))

