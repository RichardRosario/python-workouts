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
def minion_game(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    S = 0
    K = 0
    for i in range(len(string)):
        if string[i] in vowel:
            K += len(string)-i
        else:
            S += len(string)-i
    if S > K:
        print("Stuart"+" " + "%d" % S)
    elif K > S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
