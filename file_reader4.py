filename = 'file.txt'
import os
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# args = parser.parse_args()
#
# print(args.square**2)
#
def change_name(filename):
    index = filename.find('.')
    new_str = filename[:index] + '.json'
    return new_str


a = change_name(filename)
print(a)
# def rename_func(new_name):
#     os.rename(filename, new_name)
#
# rename_func('new_file.txt')
