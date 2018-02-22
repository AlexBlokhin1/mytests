a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def is_divided(some_number, i):
    return some_number % i == 0


def is_primitive_number(some_number):
    for i in range(2, int(some_number/2)):
        if is_divided(some_number, i):
            return False
    return True


def numbers(counter):
    xx = []
    for i in range(0, counter):
        if is_primitive_number(i):
            xx.append(i)
    return xx


o=numbers(1000)
print(o)

# g = is_primitive_number(11)
# print(g)
