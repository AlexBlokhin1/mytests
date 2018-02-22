
# XXXXXXXXX = ['Michael', 'John', 'Betty', 'Jacob', 'Drake', 'Alex', 'Angelina', 'Anabel', 'Simon', 'Sara', 'Andrew', 'Bill',
#          'Jack', 'Frank', '']
#
#
# def len_max(list_of_names):
#     max_len = 0
#     result_name = ""
#
#     #for name in list_of_names:
#     for i in range(0, len(list_of_names)):
#         name = list_of_names[i]
#         print('{} {}'.format(i, name))
#         current_len = len(name)
#         if current_len > max_len:
#             max_len = current_len
#             result_name = name
#     return max_len, result_name

#
# a = len_max(XXXXXXXXX)
# print(a)

import random


abc = 'bcdfghjklmnpqrstvwxz'
vowel = 'aeiouy'


def random_letter(abc):
    rand_index = random.randint(0, len(abc)-1)
    letter = abc[rand_index]
    return letter


def rand_string(abc, size):
    chars = []
    size = random.randint(1,3)
    for i in range(0, size):
        chars.append(random_letter(abc))
        # chars.append(random_letter(abc))
        chars.append(random_vowel_letter(vowel))
        chars[0] = chars[0].upper()
        result = "".join(chars)
    return result


def repeat_rand_string(a):
    result = []
    for i in range(0, a):
        result.append(rand_string(abc, i))
    return result


def random_vowel_letter(vowel):
    rand_index = random.randint(0, len(vowel)-1)
    letter = vowel[rand_index]
    return letter


a = repeat_rand_string(10)
# g = repeat_rand_string_2_vowel(1)
print(a)
