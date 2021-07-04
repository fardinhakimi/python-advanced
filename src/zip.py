

list_a = [1, 2, 3]
list_b = ['one', 'two', 'three']

zipped_list = list(zip(list_a, list_b))
zipped_set = set(zip(list_a, list_b))


print(zipped_list)
print(zipped_set)

print(zipped_list[0])
zipped_set.add((4, "FOUR"))

print(zipped_set)

if __name__ == '__main__':
    pass