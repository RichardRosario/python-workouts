# ===== Hackerrank Problems and solutions
# A valid postal code  have to fullfil both below requirements:

# must be a number in the range from to  inclusive.
# must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
from datetime import datetime as dt
import re
from collections import deque
# print(bool(re.match(
#     r'^'
#     r'(?!.*(.).\1.*(.).\2)'
#     r'(?!.*(.)(.)\3\4)'
#     r'[1-9]\d{5}'
#     r'$', input()
# )))

# ===================
# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

# Neo feels that there is no need to use 'if' conditions for decoding.

# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
# n, m = map(int, input().split())
# a, b = [], ""
# for _ in range(n):
#     a.append(input())

# for z in zip(*a):
#     b += "".join(z)

# print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

# ======================
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
# def average(array):
#     return sum(set(array)) / len(set(array))


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)
# ============================
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
# M, m = input(), set(list(map(int, input().split())))
# N, n = input(), set(list(map(int, input().split())))
# s = sorted(list(m.difference(n))+list(n.difference(m)))
# for i in s:
#     print(i)

# =================
# n, m = input().split()
# arr = [int(x) for x in input().split()]
# A = set([int(y) for y in input().split()])
# B = set([int(z) for z in input().split()])
# count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
# print(sum(count))

# =====================
# Apply your knowledge of the .add() operation to help your friend Rupal.
# num = input()
# dist = set()
# for i in range(int(num)):
#     dist.add(input())
# print(len(dist))

# =========================
# n = int(input())
# s = set(map(int, input().split()))
# q = int(input())
# for i in range(q):
#     choice = input()
#     temp = choice.split(" ")
#     if temp[0] == 'remove':
#         if int(temp[1]) in s:
#             s.remove(int(temp[1]))
#     elif temp[0] == 'discard':
#         if int(temp[1]) in s:
#             s.discard(int(temp[1]))
#     elif temp[0] == 'pop':
#         s.pop()


# print(sum(s))
# =======================
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
# n = input()
# set_n = set(map(int, input().split()))
# b = input()
# set_b = set(map(int, input().split()))
# print(len(set_n.union(set_b)))
# ========================
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
# num1, st1, num2, st2 = (set(input().split()) for i in range(4))
# print(len(st1.intersection(st2)))
# ======================
# n1 = int(input())
# set1 = set(map(int, input().split()))
# n2 = int(input())
# set2 = set(map(int, input().split()))
# print(len(set1-set2))

# =======================
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
# n1, eng = int(input()), set(input().split())

# n2, fr = int(input()), set(input().split())

# result = eng.union(fr) - eng.intersection(fr)
# print(len(result))

# =======================
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.
# m = int(input())
# A = set(map(int, input().split(" ")))
# n = int(input())

# for i in range(n):
#     cmd, args = input().split(" ")
#     B = set(map(int, input().split(" ")))
#     eval('A.'+cmd+'(B)')

# print(sum(A))
# =========================
# K = int(input())
# rooms = input().split()

# rooms.sort()
# capt_room = (set(rooms[0::2]) ^ set(rooms[1::2]))
# print(capt_room.pop())

# ======================
# You are given two sets,  A and B.
# Your job is to find whether set A is a subset of set B.
# for i in range(int(input())):
#     _, a = input(), set(map(int, input().split()))
#     _, b = input(), set(map(int, input().split()))
#     print(a.issubset(b))
# ======================
# You are given a positive integer N. Print a numerical triangle of height N-1: More than 2 lines will result in 0 score. Do not leave a blank line also
# for i in range(1, int(input())):
#     print((10**(i)//9)*i)

# a, b, m = [input().split() for _ in range(3)]
# print(pow(a, b), pow(a, b, m), sep='\n')

# a,b,c,d = (int(input()) for _ in range(4))
# print (pow(a,b)+pow(c,d))
# ===================================
# You are given a date. Your task is to find what the day is on that date.
# import calendar
# m, d, y = map(int, input().split())
# print(calendar.day_name[calendar.weekday(y, m, d)].upper())

# ==========================

# fmt = '%a %d %b %Y %H:%M:%S %z'
# for i in range(int(input())):
#     print(int(abs((dt.strptime(input(), fmt) -
#                    dt.strptime(input(), fmt)).total_seconds())))

# =================================
# You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# Note: Each input line ends with a "\n" character.
from collections import OrderedDict
# words = OrderedDict()
# for i in range(int(input())):
#     eachword = input().strip()
#     words[eachword] = words.get(eachword, 0) + 1
# print(len(words))
# print(*words.values())
# =======================
# from collections import deque
# Perform append, pop, popleft and appendleft methods on an empty deque .
# d = deque()
# for _ in range(int(input())):
#     inp = input().split()
#     getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
# print(*[item for item in d])
# ==========================
# There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube is on top of cube then sideLengthj >= sidelengthi.

# for _ in range(int(input())):
#     _, queue = input(), deque(map(int, input().split()))

#     for cube in reversed(sorted(queue)):
#         if queue[-1] == cube:
#             queue.pop()
#         elif queue[0] == cube:
#             queue.popleft()
#         else:
#             print('No')
#             break
#     else:
#         print('Yes')
#
# without using deque
# for t in range(input()):
#     input()
#     lst = map(int, input().split())
#     l = len(lst)
#     i = 0
#     while i < l - 1 and lst[i] >= lst[i+1]:
#         i += 1
#     while i < l - 1 and lst[i] <= lst[i+1]:
#         i += 1
#     print("Yes" if i == l - 1 else "No")
# ==================================
# from collections import Counter, OrderedDict


# class OrderedCounter(Counter, OrderedDict):
#     pass


# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
# ============================
# Debug the given function print_from_stream using the default value of one of its arguments.

# The function has the following signature:


# def print_from_stream(n, stream)


# This function should print the first  values returned by get_next() method of stream object provided as an argument. Each of these values should be printed in a separate line.

# Whenever the function is called without the stream argument, it should use an instance of EvenStream class defined in the code stubs below as the value of stream.
# def print_from_stream(n, stream=EvenStream()):
#     stream.__init__()
#     for _ in range(n):
#         print(stream.get_next())


# ============================
# You are given a string S.
# Your task is to find out whether S is a valid regex or not.
# for _ in range(int(input())):
#     try:
#         print(bool(re.compile(input())))
#     except re.error:
#         print('False')

# ===============================
# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# n = int(input())
# operations = [input().strip() for _ in range(n)]

# list_ = []

# commands = {
#     'insert': lambda idx, ele: list_.insert(int(idx), int(ele)),
#     'print': lambda: print(list_),
#     'remove': lambda ele: list_.remove(int(ele)),
#     'append': lambda ele: list_.append(int(ele)),
#     'sort': lambda: list_.sort(),
#     'pop': lambda: list_.pop(),
#     'reverse': lambda: list_.reverse(),
# }

# for operation in operations:
#     name, args = [i.strip() for i in (operation + ' ').split(' ', maxsplit=1)]
#     command = commands.get(name)
#     command(*args.split())

# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
print(input() == 0 or hash(tuple(map(int, input().strip().split()))))
