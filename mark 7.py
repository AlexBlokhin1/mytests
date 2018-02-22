american_names = ['Michael', 'John', 'Betty', 'Jacob', 'Drake', 'Alex', 'Angelina', 'Anabel', 'Simon', 'Sara', 'Andrew',
'Bill', 'Jack', 'Frank']


# a = name(american_names)
# print(a)
#
# counts = {}


# def func_of_elements():
#     for name in american_names:
    # if not counts.get(name):
    #     counts[name] = 1
    # else:
    #     counts[name] += 1
    # return counts


# a = func_of_elements()
# print(a)


abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# abc = 'j'


def calculate_count_of_chars(name):
    """
    Calculate number of char in NAME (input parameter)
    :param name: <string> any sequence of characters
    :return: <dict> example: {'a': 2, 'b': 1}
    """
    result = {}
    for char in name:
        if not result.get(char):
            result[char] = 0
        result[char] += 1
    return result


def counter():
    result = {}
    for index in range(0, len(abc)):
        letter = abc[index]
        for m in range(0, len(american_names)):
            per_name = calculate_count_of_chars(american_names[m])
            for key in per_name.keys():
                count = per_name[key]
                if key == letter:
                    if not result.get(key):
                        result[key] = 0
                        result[key] += 1
                print("key: {} : Count {}".format(key, count))
    return result


print(counter())
# a = calculate_count_of_chars(american_names[1])
# print(a)
