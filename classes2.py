#!/usr/bin/env

import random
mark_of_car = ['Mersedes', 'Audi', 'Dodge', 'Lada', 'Volvo']
color_of_car = ['green', 'yellow', 'black', 'white', ]
engine_of_car = ['V8', 'V12']
number_of_doors = ['two doors', 'four doors']


class Car():

    def __init__(self):
        self.color = None
        self.mark = None
        self.engine = None

    def __str__(self):
        return "I am cool {} {} with {}  engine.".format(self.color, self.mark, self.engine)

    def random_mark(self):
        rand_index = random.randint(0, len(mark_of_car)-1)
        mark = mark_of_car[rand_index]
        self.mark = mark

    def random_color(self):
        rand_index = random.randint(0, len(color_of_car)-1)
        self.color = color_of_car[rand_index]

    def random_engine(self):
        rand_index = random.randint(0, len(engine_of_car)-1)
        self.engine = engine_of_car[rand_index]


class LiteCar(Car):
    def __init__(self, roomines):
        self._roomines = roomines
        super().__init__()

    def __str__(self):
        return 'My roomines is {} people'.format(self.roomines)

    def set_roomines(self, value):
        print("FUNCTION INVOKE")
        self._roomines = value

    @property
    def roomines(self):
        return self._roomines


class Lorry(Car):

    def __init__(self, weight=0.0):
        self.weight = weight
        super().__init__()

    def __str__(self):
        if self.weight > 2:
            return 'I am lory, my weight = {}t. '.format(self.weight)
        else:
            return super().__str__()

    def set_weight(self, value):
        self.weight = value


my_new_car = LiteCar(4)
my_new_car.set_roomines(77)
print("ROOMS: {}".format(my_new_car.roomines))
my_new_car.random_color()
my_new_car.random_engine()
my_new_car.random_mark()


print(my_new_car)
