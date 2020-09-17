import re
import numpy

# hackerrank problems and solutions

# =================== You are given two arrays:  and .
# Your task is to compute their inner and outer product.
# A = numpy.array(input().split(), int)
# B = numpy.array(input().split(), int)

# print(numpy.inner(A, B))
# print(numpy.outer(A, B))

# ==================================

from itertools import combinations, product

# N = int(input())
# S = input().split()
# K = int(input())

# num = 0
# den = 0

# for c in combinations(S, K):
#     den += 1
#     num += 'a' in c

# print(float(num)/den)

# =============================
# You are given a function . You are also given  lists. The  list consists of  elements.
# You have to pick one element from each list so that the value from the equation below is maximized:
# The first line contains 2 space separated integers K and M.
# The next  lines each contains an integer N, denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.
# K, M = map(int, input().split())
# N = (list(map(int, input().split())) for _ in range(1, K)) -- first option
# N = (list(map(int, input().split()))[1:] for _ in range(K)) -- best option

# results = map(lambda x: sum(i**2 for i in x) % M, product(*N))

# version 2
# print(max(sum(j) % M for j in product(
#     *((int(i) ** 2 for i in input().split()[1:]) for _ in range(K)))))

# print(max(results))

# ==================
# v = "aeiou"
# c = "qwrtypsdfghjklzxcvbnm"
# print(*re.findall("(?=[%s]([%s]{2,})[%s])" %
#                   (c, v, c), input(), re.I) or [-1], sep="\n")

# =======================

# s = 'halhsdflasasdf'
# k = 'alsdlajsgjpirpnapv'
# if k in s:
#     print(*[(i.start(), (i.start()+len(k)-1))
#             for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
# else:
#     print('(-1, -1)')

# =====================
# import re
# N = int(input())

# for i in range(N):
#     print(re.sub(r'(?<= )(&&|\|\|)(?= )',
#                  lambda x: 'and' if x.group() == '&&' else 'or', input()))
# ====================
# thou = "(?:(M){0,3})?"
# hun = "(?:(D?(C){0,3})|(CM)|(CD))?"
# ten = "(?:(L?(X){0,3})|(XC)|(XL))?"
# unit = "(?:(V?(I){0,3})|(IX)|(IV))?"

# regex_pattern = r"^" + thou + hun + ten + unit + "$"

# print(str(bool(re.match(regex_pattern, input()))))
# ================================ regex to check mobile phone

# for _ in range(int(input())):
#     if re.match(r'[789]\d{9}$', input()):
#         print('YES')
#     else:
#         print('NO')
# ====================  Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

# import email.utils
# N = input()
# for _ in range(int(N)):
#     email_inpt = email.utils.parseaddr(input())

#     if bool(re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$', email_inpt[1])):
#         print(email.utils.formataddr(email_inpt))
# =======================
N = input()
for i in range(0, N):
    matches = re.findall(
        r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", input(), re.IGNORECASE)
    for m in matches:
        print(m)
