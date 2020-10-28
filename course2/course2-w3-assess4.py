# python course 2.. week 3 assessment 4
def int_return(x):
    return x


def add(num):
    return num + 2


def change(str):
    return str + "Nice to meet you!"


def accum(lst):
    sum = 0
    for num in lst:
        sum = sum + num
    return sum


lst = [1, 2, 3, 4, 5, 6, 7]
print(accum(lst))


def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    if len(lst) < 5:
        return "Less than 5"


def divide(x):
    res = x / 2
    return res


def sum(y):
    ans = divide(y) + 6
    return ans
