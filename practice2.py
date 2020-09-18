# ===== Hackerrank Problems and solutions
# A valid postal code  have to fullfil both below requirements:

# must be a number in the range from to  inclusive.
# must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
import re
print(bool(re.match(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$', input()
)))
