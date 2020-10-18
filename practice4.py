# You are given a string S consisting only of digits 0-9, commas ,, and dots .

# Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the, and . symbols in S.
#
import numpy as np
import numpy
import re
regex_pattern = r""  # Do not delete 'r'.

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

N, M, P = map(int, input().split())
arrA = np.array([input().split() for _ in range(N)], int)
arrB = np.array([input().split() for _ in range(M)], int)
print(np.concatenate((arrA, arrB), axis=0))
