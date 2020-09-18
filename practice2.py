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
n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

# print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
