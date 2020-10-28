# # 1--
# def mult(x, y=6):
#     return x*y

# # 2--


# def greeting(name, greeting="Hello ", excl="!"):
#     return greeting + name + excl


# print(greeting("Bob"))
# print(greeting(""))
# print(greeting("Bob", excl="!!!"))


# # 3---


# def sum(intx, intz=5):
#     return intz + intx

# # 4--


# def test(x, y=True, dict1={2: 3, 4: 5, 6: 8}):
#     if y == True:
#         return dict1[x]
#     return False

# 5--
# Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.


# But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is , it should return False.


# def checkingIfIn(str, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
#     if direction == True:
#         if str in d:
#             return True
#         else:
#             return False

#     else:
#         if str not in d:
#             return True
#         else:
#             return False

# 6--

def checkingIfIn(a, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]


c_false = checkingIfIn('beans')
print(c_false)
c_true = checkingIfIn(
    'apple', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
print(c_true)
fruit_ans = checkingIfIn('fruit')
print(fruit_ans)
param_check = checkingIfIn('watermelon')+1
