# ITERATORS

print("ITERATORS")

list_of_names = ['fardin', 'hayah', 'fardin2']

list_of_names_iter = iter(list_of_names)

print(next(list_of_names_iter))
print(next(list_of_names_iter))
print(next(list_of_names_iter))


for k, v in enumerate(list_of_names, start= 1):
    print(k, v)


if __name__ == '__main__':
    pass
