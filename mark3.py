def figure(index):
    for i in range(1, index+1):
        rand = 2 ** i
        print('2**{} = {}'.format(i, rand))


figure(10)
