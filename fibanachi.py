def fibanachi_numbers(m):
    xx = [1]
    for i in range(0, m):
        b = xx[i] + xx[i-1]
        xx.append(b)
    return xx


def rfib(m, buff):
    if m < 2:
        buff.append(1)
        return 1
    m = m + rfib(m-1, buff)
    buff.append(m)
    return m



buff = []
print(rfib(10, buff))
print(buff)

# m = fibanachi_numbers(3)
# print(m)
#
# m = fibanachi_numbers(4)
# print(m)
#
# m = fibanachi_numbers(5)
# print(m)
#

#m = fibanachi_numbers(6, buff)
# print(m)

