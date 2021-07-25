# import random as rd
# from random import randint as ri
#
# print(ri(1,2))
#


# from sys import argv
#
# sum_args = int(argv[1]) + int(argv[2])
# print(sum_args)

#random_list = [x for x in range(50) if x % 1 == 1]

# random_list = [i*j for i in range(10) for j in range(10)]
# random_list = []
# for i in range(50):
#     if i % 2 == 0:
#         random_list.append(i)
#print(random_list)
#
# random_dict = {x:chr(x) for x in range(50) if x % 2 ==1}
#
# print(random_dict)


from random import randint, randrange, random


#rand_int = randint(-50, 50)
#rand_int = randrange(5, 10, 2)
# rand_float = round(random() * 10, 2)
#
# print(rand_float)

# def first_generator(num):
#     for i in range(num):
#         yield i
#
# gen = first_generator(10000)
#
# for i in gen: #вызывается next(gen)
#     print(i)
#
# for i in range(50):
#     print(i)

# gen = (i for i in range(10))
#
# print(gen)

# from functools import reduce, partial
#
# def div_nums(prev, next):
#     return prev + next
#a = [1, 2, 3, 4, 6, 1, 2]
#a = ['ssfd', 'dc']
# print(reduce(div_nums, a))

# def div_nums(a, b):
#     return a / b
#
# my_div_nums = partial(div_nums, b = 2)
# print(my_div_nums(10))

from itertools import count, cycle
#
# for i in count(1):
#     print(i)
#     if i == 100:
#         break

# a = [x for x in range(20)]
# b_list = ['green', 'blue', 'red']
# gen = cycle(b_list)
# for i in count(1, 5):
#     print(f'{i} - {next(gen)}')
#
import math

print(math.floor(7.5))
print(math.ceil(7.5))
