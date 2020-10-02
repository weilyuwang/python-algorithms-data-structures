import sys

x = [i**2 for i in range(10000)]


def gen(n):
    for i in range(n):
        yield i ** 2


g = gen(10000)


print(sys.getsizeof(x))
print(sys.getsizeof(g))
