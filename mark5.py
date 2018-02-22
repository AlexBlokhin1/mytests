import random

names = ['Michael', 'John', 'Betty', 'Jacob', 'Drake', 'Alex', 'Angelina', 'Anabel', 'Simon', 'Robert']
#
# print(names)


def last_letter(name, letter):
    return name[-1] == letter


def first_letter(name, letter):
    return name[0] == letter


def random_list(max_count):
    xx = []
    while True:
        if len(xx) == max_count:
            break
        rand_index = random.randint(0, max_count)
        name = names[rand_index]

        # if last_letter(name, 'a') or last_letter(name, 'l') :
        #     xx.append(name)
        # if first_letter(name, 'B'):
        #     xx.append(name)

        if name[0] in ["J", "S"]:
            xx.append(name)

    return xx


a = random_list(9)
print(a)
