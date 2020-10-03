# ========================
# One of the built-in functions of Python is divmod, which takes two arguments  and  and returns a tuple containing the quotient of  first and then the remainder .
# a, b = int(input()), int(input())
# print(a//b, a % b, divmod(a, b), sep='\n')

# ===========================
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets + 1 point for each occurrence of the substring in the string .
# def minion_game(string):
#     vowel = ['A', 'E', 'I', 'O', 'U']
#     S = 0
#     K = 0
#     for i in range(len(string)):
#         if string[i] in vowel:
#             K += len(string)-i
#         else:
#             S += len(string)-i
#     if S > K:
#         print("Stuart"+" " + "%d" % S)
#     elif K > S:
#         print("Kevin"+" "+'%d' % K)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
# ==========================================
# Consider the following:

# A string, s, of length n.
# An integer, k, where k is a factor of n.
# We can split s into n/k  subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string u such that:

# The characters in u are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that each character in u occurs exactly once. In other words, if the character at some index j in  ti occurs at a previous index <j in ti, then do not include the character in string ui.
# Given s and k, print n/k lines where each line i denotes string u.
# import operator
# from functools import reduce
# from fractions import Fraction


# def merge_the_tools(string, k):
#     while string:
#         s = string[0:k]
#         seen = ''
#         for c in s:
#             if c not in seen:
#                 seen += c
#         print(seen)
#         string = string[k:]


# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

# ========================
# reduce operator
# Given a list of rational numbers,find their product.

# Concept
# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say[1, 2, 3] and you have to find its sum.


# def product(fracs):
#     # complete this line with a reduce statement
#     t = reduce(operator.mul, fracs)
#     return t.numerator, t.denominator


# if __name__ == '__main__':
#     fracs = []
#     for _ in range(int(input())):
#         fracs.append(Fraction(*map(int, input().split())))
#     result = product(fracs)
#     print(*result)
# ===============================
# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
# def print_rangoli(size):
#     # your code goes here
#     from string import ascii_lowercase as chars
#     heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])
#              ).center(4*n-3, '-')for i in range(n)]
#     print(*(heap[::-1]+heap[1:]), sep="\n")


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
# ====================================
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

# def capitalize(s):
#     for x in s[:].split(" "):
#         s = s.replace(x, x.capitalize())
#         s = "".join(s)
#     return s
# ==================================
# For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

# The real and imaginary precision part should be correct up to two decimal places.
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self, no):
#         a = self.real+no.real
#         b = self.imaginary+no.imaginary
#         if a < 0 and b < 0:
#             return ("-%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b < 0:
#             return ("%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a < 0 and b >= 0:
#             return ("-%.2f+%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b >= 0:
#             return ("%.2f+%.2fi" % (abs(a), abs(b)))

#     def __sub__(self, no):
#         a = self.real-no.real
#         b = self.imaginary-no.imaginary
#         if a < 0 and b < 0:
#             return ("-%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b < 0:
#             return ("%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a < 0 and b >= 0:
#             return ("-%.2f+%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b >= 0:
#             return ("%.2f+%.2fi" % (abs(a), abs(b)))

#     def __mul__(self, no):
#         a = self.real*no.real-self.imaginary*no.imaginary
#         b = no.imaginary*self.real+self.imaginary*no.real
#         if a < 0 and b < 0:
#             return ("-%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b < 0:
#             return ("%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a < 0 and b >= 0:
#             return ("-%.2f+%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b >= 0:
#             return ("%.2f+%.2fi" % (abs(a), abs(b)))

#     def __truediv__(self, no):
#         x = no.real**2+no.imaginary**2
#         a = (self.real*no.real+self.imaginary*no.imaginary)/x
#         b = (-no.imaginary*self.real+self.imaginary*no.real)/x
#         if a < 0 and b < 0:
#             return ("-%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b < 0:
#             return ("%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a < 0 and b >= 0:
#             return ("-%.2f+%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b >= 0:
#             return ("%.2f+%.2fi" % (abs(a), abs(b)))

#     def mod(self):
#         a = pow(self.real**2+self.imaginary**2, 0.5)
#         b = 0
#         if a < 0 and b < 0:
#             return ("-%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b < 0:
#             return ("%.2f-%.2fi" % (abs(a), abs(b)))
#         elif a < 0 and b >= 0:
#             return ("-%.2f+%.2fi" % (abs(a), abs(b)))
#         elif a >= 0 and b >= 0:
#             return ("%.2f+%.2fi" % (abs(a), abs(b)))
# =======================================
# You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.
import sys
import xml.etree.ElementTree as etree


# def get_attr_number(node):
#     # your code goes here
#     out = len(node.attrib)
#     return out+sum((get_attr_number(child) for child in node))


# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))

# You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.
maxdepth = 0


def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
