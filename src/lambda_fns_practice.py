
from functools import reduce

uppercase_list = list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
filtered_list = list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
reduced_list = reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])


names = ['fardin']
print(list(map(lambda  x: x.upper(), names)))
print([uppercase_list, filtered_list, reduced_list])


if __name__ == '__main__':
    pass
