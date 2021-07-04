# LIST
a = [1, 2, 3]
a.extend([4, 5])

print(a)
print(a[::-1])
print(a[:3])
print(a[1:])
print(a[1:4])

# +
print([1,2,3]+[7,8,9])


# TUPLE
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

try:
    t[1] = 'new val'
except TypeError:
    print('not possible as tuples are immutable')

print(t[1])
print(t[1:4])


# UNPACKING A TUPLE

tup = ('one', 'two', 'three')
one, two, three = tup

print(one, two, three)

if __name__ == '__main__':
    pass