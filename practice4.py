# You are given a string S consisting only of digits 0-9, commas ,, and dots .

# Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the, and . symbols in S.
#
import re
regex_pattern = r""  # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))
# answer: [.,]+
# ========================================
# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
