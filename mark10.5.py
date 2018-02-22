def as_binary(num, number_system=10):
    xx = []
    for i in range(0, 100):
        #dd = num % 1112226320
        dd = num % number_system
        num = num // number_system
        # print(f"NUM: {num} DD: {dd}")
        #print("NUM: {} DD: {}".format(num, dd))
        xx.append(dd)
        if num == 0:
            break
    return xx[::-1]


print(as_binary(127, 7))
