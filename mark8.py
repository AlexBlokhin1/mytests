import random
import collections

american_names = ['Michael', 'John', 'Betty', 'Jacob', 'Drake', 'Alex', 'Angelina', 'Anabel', 'Simon', 'Sara', 'Andrew', 'Bill',
'Jack', '  llll']


abetka = 'abcdefghijklmnopqrstuvwxyz'


def random_chars(abc, size=10):
    result_chars = []
    for i in range(0, size):
        rand_index = random.randint(0, len(abc)-1)
        letter = abc[rand_index]
        result_chars.append(letter)
    return result_chars


def check_names(american_names, xname, direction="max"):
    counters = {}
    counters = collections.defaultdict(int)

    actual_characters_count = 0 if direction == "max" else 100000
    actual_name_count = ''

    for name in american_names:
        for char in name.lower():
            if char in xname:
                counters[name] += 1

    # for name in american_names:
    #     for char in name.lower():
    #         if char in xname:
    #             if counters.get(name):
    #                 counters[name] += 1
    #             else:
    #                 counters[name] = 1

    for key in counters.keys():
        current_value = int(counters[key])
        if (direction == "max" and current_value > actual_characters_count) or (direction == 'min' and current_value < actual_characters_count):
            actual_characters_count = current_value
            actual_name_count = key

    return actual_characters_count, actual_name_count


if __name__ == "__main__":
    abc = random_chars(abetka, 12)
    abc_str = "".join(abc)
    # abc_lst = abc_str.split()
    max_name = check_names(american_names, abc_str, "max")
    min_name = check_names(american_names, abc_str, "min")
    # print("type: {} abc: {}".format(type(abc_str), abc_str))
    print(max_name)
    print(min_name)
