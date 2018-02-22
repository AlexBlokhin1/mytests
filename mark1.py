for i in range(5, -1, -1):
     if i % 2:
         print("Hello [{}]".format(i))
     else:
         print("hello Vasya")


def hello_micro(count, message, rate):
    for i in range(1, count):
        print(message)


hello_micro(7, "Vasya", 3)
print('')
hello_micro(2, "Petya", 6)

import random

messages = ['Hello', 'Whats up?', 'How are you?', 'How do you do?', 'Hi']
for message in messages:
     print(message)


index = random.randint(0, len(messages)-1)
for i in range(1, 6):
    print('{}) {}'.format(i, messages[index]))

print("  ")
print(index)


def random_message(msg):
    index = random.randint(0, len(msg)-1)
    print(msg)
    print(msg[index])


random_message(messages)

messages = ['Hello', 'Whats up?', 'How are you?', 'How do you do?', 'Hi']

