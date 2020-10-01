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
import operator
from functools import reduce
from fractions import Fraction


def merge_the_tools(string, k):
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

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
def print_rangoli(size):
    # your code goes here
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])
             ).center(4*n-3, '-')for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
