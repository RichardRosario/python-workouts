# 1---
# def sublist(lst):
#     count = 0
#     newlst = []
#     while count < len(lst):
#         if lst[count] != 5:
#             newlst.append(lst[count])
#         else:
#             break
#         count = count + 1
#     return newlst


# inputlst = input()
# inputlst = inputlst.split()
# print(sublist(inputlst))

# 2---
# def check_nums(lst):
#     num = 0
#     nums = []
#     while num < len(lst):
#         if lst[num] != 7:
#             nums.append(lst[num])
#         else:
#             break
#         num = num + 1
#     return nums

# 3---
# lst = [4, 5, 6, 7, 87, 8, 8]
# check_nums(lst)
# print(check_nums)

# 3--
# def sublist(strlist):
#     count = 0
#     newlist = []
#     while count < len(strlist):
#         if strlist[count] != "STOP":
#             newlist.append(strlist[count])
#         else:
#             break
#         count = count + 1
#     return newlist


# strlist = ['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']

# 4---
# def stop_at_z(str):
#     word = 0
#     newlist = []
#     while word < len(str):
#         if str[word] != "z":
#             newlist.append(str[word])
#         else:
#             break
#         word = word + 1
#     return newlist


# string = 'majfguarnafgmzjng'
# print(stop_at_z(string))

# 5---
# sum1 = 0

# lst = [65, 78, 21, 33]

# for x in lst:
#     sum1 = sum1 + x

# x = 0
# sum2 = 0
# while x < len(lst):
#     sum2 = sum2 + lst[x]
#     x = x + 1
# print(sum2)

# 6---


def beginning(list):
    count = 0
    newlist = []

    while count < len(list):
        if list[count] != "bye":
            newlist.append(list[count])
        else:
            break
        count = count + 1
    return newlist[0:10]
