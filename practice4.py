# You are given a string S consisting only of digits 0-9, commas ,, and dots .

# Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the, and . symbols in S.
#
import numpy as np
import numpy
import re
# regex_pattern = r""  # Do not delete 'r'.

# print("\n".join(re.split(regex_pattern, input())))
# answer: [.,]+
# ========================================
# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.
# m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
# print(m.group(1) if m else -1)
# ============================
# numpy array
# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.
#


# def arrays(arr):
#     return(numpy.array(arr[::-1], float))


# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)
# ==============================
# shape and reshape with numpy
# print(np.array(input().split(), int).reshape(3, 3))

# You are given a NxM integer array matrix with space separated elements ( N= rows and  M= columns).
# Your task is to print the transpose and flatten results.

# N, M = map(int, input().split())
# array = np.array([input().strip().split() for _ in range(N)], int)
# print(array.transpose())
# print(array.flatten())

# ===============================
# You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

# N, M, P = map(int, input().split())
# arrA = np.array([input().split() for _ in range(N)], int)
# arrB = np.array([input().split() for _ in range(M)], int)
# print(np.concatenate((arrA, arrB), axis=0))

# ================================
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# def swap_case(s):
#     return s.swapcase()


# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# ==================string split and join
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.


# def split_and_join(line):
#     # write your code here
#     x = line.split(" ")
#     x = "-".join(x)
#     return x


# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
# ==================================
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.


# def print_full_name(a, b):
#     print("Hello {} {}! You just delved into python.".format(first_name, last_name))


# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# ===============================
# mutations
# Read a given string, change the character at a given index and then print the modified string.


# def mutate_string(string, position, character):
#     return string[:position] + character + string[position + 1:]


# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# ================================
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)

# ===============================================
# You are given a string S.
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    S= input()
    print(any(c.isalnum() for c in S))
    print(any(c.isalpha() for c in S))
    print(any(c.isdigit() for c in S))
    print(any(c.islower() for c in S))
    print(any(c.isupper() for c in S))
