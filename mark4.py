import random


def my_random():
    i = random.randint(0, 5)
    if i % 5 == 0:
        return i


b = my_random()
print(b)


def random_numbers(index):
    for i in range(1, index+1):
        c = random.randint(0, 200)
        a = my_random()
        if a % 2 == 0:
            print('{}) {} '.format(i, c))

        if a % 17 == 0:
            print('Bingo = {}'.format(a))
        return a


aaa = random_numbers(10)
print(aaa)
