import random


def random_numbers(number, figure):
    for index in range(1, number):
        numbers = random.randint(0, figure)
        print('{}) {}'.format(index, numbers))

random_numbers(10, 10)