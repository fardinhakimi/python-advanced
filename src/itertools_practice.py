import itertools


list_of_names = ['fardin', 'hayah', 'fardin2']

print("\n PERMUTATIONS: \n")

# all possible mutations of a given set
for name in itertools.permutations(list_of_names):
    print(name)


print("\n COMBINATIONS: \n")
for name in itertools.combinations(list_of_names, 2):
    print(name)


print(any([1,2,0,5]))
print(all([1,2,0,5]))

print(list(itertools.dropwhile(lambda name: name !='fardin2', list_of_names)))
print(list(itertools.takewhile(lambda name: name !='fardin2', list_of_names)))


if __name__ == '__main__':
    pass