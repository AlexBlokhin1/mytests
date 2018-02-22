import random

XXXXXXXXX = ['Michael', 'John', 'Betty', 'Jacob', 'Drake', 'Alex', 'Angelina', 'Anabel', 'Simon', 'Sara', 'Andrew', 'Bill',
         'Jack', 'Frank']


# def even_letters(names):
#     xx = []
#     for i in range(0, len(names)):
#         name = names[i]
#         if len(name) % 2 == 0:
#             print('{} {} '.format(i, name))
#             xx.append(name)
#     return xx


def count_numbers(names):
    xx = []
    for i in range(0, len(names)):
        name = names[i]
        if len(name) % 2 !=0:
            print('{} {}'.format(i, name))
            xx.append(name)
    return len(xx)


#a = even_letters(XXXXXXXXX, 12)
a = count_numbers(XXXXXXXXX)
#a = even_letters(["Basil", "Alex"])
print(a)



