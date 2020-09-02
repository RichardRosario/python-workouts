L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
# normal way
for i in range(len(L1)):
    L3.append(L1[i] + L2[i])
# print(L3)


# using map and lambda
L5 = map(lambda x: x[0] + x[1], zip(L1, L2))
# print(L5)

# using zip function and for loop
ls = list(zip(L1, L2))
l3 = []
# print(ls)
for (x1, x2) in ls:
    l3.append(x1+x2)
# print(l3)

# using zip and comprehension
l4 = [x1 + x2 for x1, x2 in list(zip(L1, L2))]
# print(l4)


# ========\\
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


# print(possible("wonderwall", "_on__r__ll", "otnqurl"))
# print(possible("wonderwall", "_on__r__ll", "wotnqurl"))


# using zip
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))


# === Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be accomplished in one line of code

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [(x1+x2) for (x1, x2) in list(zip(L1, L2)) if (x1 > 10 and x2 < 5)]
print(L3)
