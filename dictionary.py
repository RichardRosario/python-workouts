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
# check how many key is greater than 1
for key in char_d:
    if char_d[key] > 1:
        (key, char_d[key])
        # print(char_d)


schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3,
            "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

total_credits = 0
tot_keys = []

for key in schedule.keys():
    tot_keys.append(key)
for v in schedule.values():
    total_credits += v
# print(tot_keys)
# print(total_credits)

# ==============================
product = "iphone and android phones"


def split(product):
    return [char for char in product]


lst = split(product)
lett_d = {}

for char in lst:
    if char in lett_d:
        lett_d[char] += 1
    else:
        lett_d[char] = 1
# print(lett_d)


ks = list(lett_d.keys())
# print(ks)
max_value = ks[0]

for k in ks:
    if lett_d[k] > lett_d[max_value]:
        max_value = k

# print(max_value)

# check the number of items===========


def count(nums):
    return len(nums)


print(count([1, 2, 3, 4, 4]))
