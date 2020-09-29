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
