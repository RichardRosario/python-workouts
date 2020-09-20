# ===== Hackerrank Problems and solutions
# A valid postal code  have to fullfil both below requirements:

# must be a number in the range from to  inclusive.
# must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
import re
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
n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    choice = input()
    temp = choice.split(" ")
    if temp[0] == 'remove':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
    elif temp[0] == 'discard':
        if int(temp[1]) in s:
            s.discard(int(temp[1]))
    elif temp[0] == 'pop':
        s.pop()


# print(sum(s))
