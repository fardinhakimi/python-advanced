from random import (choices, randint, randrange, shuffle, sample)

print(choices(['choice1', 'choice2', 'choice3']))

print(shuffle(['CARD1', 'CARD2', 'CARD3']))

print(randint(1, 10))
print(randrange(100))
print(randrange(2, 10))

print(sample([x for x in range(1, 100)], 5))

if __name__ == '__main__':
    pass

