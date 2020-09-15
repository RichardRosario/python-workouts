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

N = int(input())
S = input().split()
K = int(input())

num = 0
den = 0

for c in combinations(S, K):
    den += 1
    num += 'a' in c

# print(float(num)/den)

# =============================
# You are given a function . You are also given  lists. The  list consists of  elements.
# You have to pick one element from each list so that the value from the equation below is maximized:
# The first line contains 2 space separated integers K and M.
# The next  lines each contains an integer N, denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.
K, M = map(int, input().split())
#N = (list(map(int, input().split())) for _ in range(1, K))
N = (list(map(int, input().split()))[1:] for _ in range(K))

results = map(lambda x: sum(i**2 for i in x) % M, product(*N))

# print(max(results))
