# hackerrank problems and solutions
from itertools import combinations_with_replacement, groupby
from itertools import permutations, product, combinations
import numpy

# addition_str = "2+5+10+20"
# nums = addition_str.split("+")
# sum_val = 0

# for num in nums:
#     nums += num
# # print(sum_val)


# def adding(x):
#     y = 3
#     z = y + x + x
#     print(z)
#     return z


# adding(4)


# def producing(x):
#     z = x * y
#     return z


# print(producing(adding(4)))

# ============
# You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.


# def divide(x):
#     return x / 2
# def sum(y):
#     return divide(y) + 6


# print(sum(4))
# print(divide(3))

# ===== Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.
# list1 = [8, 3, 4, 5, 6, 7, 9]

# tot = 0
# for elem in list1:
#     tot = tot + elem

# i = 0
# accum = 0
# while i < len(list1):
#     accum = accum + list1[i]
#     i += 1
# print(tot)
# print(accum)

# ===== Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


# def check_nums(nums):
#     new_nums = []
#     i = 0
#     while i < len(nums):
#         if nums[i] != 7:
#             break
#         new_nums.append(nums[i])
#         i += 1
#     return new_nums


# list = [1, 2, 3, 4, 7, 8, 9]
# print(check_nums(list))
# =======================
# for n in range(2, 5):
#     if n % 2 == 0:
#         print("Not Weird")
#     elif n % 2 == 1:
#         print('Weird')
# for n in range(6, 20):
#     if n % 2 == 0:
#         print('Weird')
#     elif n > 20:
#         print('Not Weird')

# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}

# print(check[
#     n % 2 == 0 and (
#         n in range(2, 6) or
#         n > 20)
# ])


# a = 3
# b = 2
# c = a+b
# d = a-b
# e = a*b

# print('{}\n{}\n{}'.format(a+b, a-b, a*b))
# =================================
# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.
# a = 6
# b = 5
# c = a//b
# d = a/b
# print('{}\n{}'.format(a//b, a/b))
# n = 3

# for i in range(5):
# print(i**2)
# ================================
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.


# def is_leap(year):
#     leap = False
# wihtout if statement
# return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
# with if statement
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     leap = True
# return leap


# print(is_leap(2022))
# ====================================
# Print the list of integers from  through  as a string, without spaces.
# n = [i for i in range(5)]
# for i in range(5):
#     n.append(i)
# print(n)
# new_n = ''.join(str(i) for i in n)
# print(new_n)
# n = 3
# # print(*range(1, int(input())+1), sep='')
# # print(*range(1, int(input())+1), sep='')
# for i in range(1, n+1):
#     print(f"{i}", end='')
# =============================
# ints = tuple(map(int, input().split()))
# print(numpy.zeros(ints, dtype=numpy.int))
# print(numpy.ones(ints, dtype=numpy.int))
# print(numpy.eye(ints, k=0))
# ============================
# The first line contains two space separated integers,  and .
# The next  lines contains  space separated integers of array .
# The following  lines contains  space separated integers of array .
# N, M = map(int, input().split())

# A, B = (numpy.array([input().split()
#                      for _ in range(N)], dtype=int) for _ in range(2))
# print(A + B)
# print(A - B)
# print(A * B)
# print(A / B)
# print(A % B)
# print(A ** B)
# ===================
# numpy.set_printoptions(sign=' ')

# A = numpy.array(input().split(), float)

# print(numpy.floor(A))
# print(numpy.ceil(A))
# print(numpy.rint(A))
# =================================
# N, M = map(int, input().split())
# my_array = numpy.array([input().split() for i in range(N)], int)

# print(numpy.prod(numpy.sum(my_array, axis=0),axis=0))
# ===================
# N, M = map(int, input().split())

# my_arr = numpy.array([input().split() for i in range(N)], int)

# print(numpy.max(numpy.min(my_arr, axis=1)))
# ==============================
# numpy.set_printoptions(sign=' ')
# N, M = map(int, input().split())

# my_arr = numpy.array([input().split() for i in range(N)], int)

# numpy.set_printoptions(legacy='1.13')
# print(numpy.mean(my_arr, axis=1))
# print(numpy.var(my_arr, axis=0))
# print(numpy.std(my_arr))

# =======================
# N = int(input())
# A = numpy.array([input().split() for _ in range(N)], int)
# B = numpy.array([input().split() for _ in range(N)], int)
# print(numpy.dot(A, B))

# ================== get the determinant
# N= int(input())
# a=numpy.array([input().split() for _ in range(N)],float)
# numpy.set_printoptions(legacy='1.13')
# print(numpy.linalg.det(a))
# You are given a two lists  and . Your task is to compute their cartesian product X.

# using comprehension
# A = [int(x) for x in input().split()]
# B = [int(x) for x in input().split()]
# # using list and map
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(*product(A, B))
# print(*product(a, b))
# ======================You are given a string .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
# s, n = input().split()

# perm = list(permutations(s, int(n)))
# perm.sort()
# [print("".join(i)) for i in perm]
# =========================
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
# S, k = input().split()

# for i in range(1, int(k)+1):
#     for c in combinations(sorted(S), i):
# print(''.join(c))

# ===================You are given a string .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
# S, k = input().split()

# comb = list(combinations_with_replacement(sorted(S), int(k)))
# for c in comb:
# print("".join(c))

# =================
# one liner
# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
