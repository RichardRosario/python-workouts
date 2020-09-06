# str into dictionary
stri = "what can I do"


def split(stri):
    return [char for char in stri]


lst = split(stri)
char_d = {}

for s in lst:
    if s in char_d:
        char_d[s] += 1
    else:
        char_d[s] = 1

print(char_d)
