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
# N = input()
# for i in range(0, N):
#     matches = re.findall(
#         r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", input(), re.IGNORECASE)
#     for m in matches:
#         print(m)

# ========================You are given an HTML code snippet of  lines.
# Your task is to print start tags, end tags and empty tags separately.
# You are given an HTML code snippet of  lines.
# Your task is to print start tags, end tags and empty tags separately.

from html.parser import HTMLParser


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('Start :', tag)
#         for ele in attrs:
#             print('->', ele[0], '>', ele[1])

#     def handle_endtag(self, tag):
#         print('End   :', tag)

#     def handle_startendtag(self, tag, attrs):
#         print('Empty :', tag)
#         for ele in attrs:
#             print('->', ele[0], '>', ele[1])


# N = input()
# parser = MyHTMLParser()
# for _ in range(int(N)):
#     parser.feed(input())


# class CustomHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         number_of_line = len(data.split('\n'))
#         if number_of_line > 1:
#             print('>>> Multi-line Comment')
#         else:
#             print('>>> Single-line Comment')
#         if data.strip():
#             print(data)

#     def handle_data(self, data):
#         if data.strip():
#             print(">>> Data")
#             print(data)
# N= input()
# parser = CustomHTMLParser()
# set initial value of html string
# html_str = ''
# loop through the input
# for _ in range(int(N)):
#     html_str += input().rstrip()+'\n'

# parser.feed(html_str)
# parser.close()

# =========================
# You are given an HTML code snippet of  lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         [print('-> {} > {}'.format(*attr)) for attr in attrs]


# html_str = '\n'.join([input() for _ in range(int(input()))])
# parser = MyHTMLParser()
# parser.feed(html_str)
# parser.close()

# =======================
# ABCXYZ company has up to  employees.
# The company decides to create a unique identification number(UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
# A valid UID must follow the rules below:

# It must contain at least  uppercase English alphabet characters.
# It must contain at least  digits(-).
# It should only contain alphanumeric characters(-,  - & -).
# No character should repeat.
# There must be exactly  characters in a valid UID.


# [print('Valid') if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', input(
# )) else print('Invalid') for _ in range(int(input()))]

# N = input('B1CD102354')
# for _ in range(int(N)):
#     if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', input(
#     )):
#         print('Valid')
#     else:
#         print('Invalid')

# Explanation:

# (?!.*(.).*\1) checks no repeating characters
# (?=(?: .*[A-Z]){2, }) checks at least 2 uppercase letters
# (?=(?: .*\d){3, }) checks at least 3 digits
# [a-zA-Z0-9]{10} checks exactly 10 alphanumeric characters.

# ================================
# Checking a valid credit card. You want to verify whether credit card numbers are valid or not.

# A valid credit card from ABCD Bank has the following characteristics:

# ► It must start with a ,  or .
# ► It must contain exactly  digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.
cc_check = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

for _ in range(int(input().strip())):
    if cc_check.search(input().strip()):
        print('Valid')
    else:
        print("Invalid")
