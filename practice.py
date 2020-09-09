addition_str = "2+5+10+20"
nums = addition_str.split("+")
sum_val = 0

# for num in nums:
#     nums += num
# # print(sum_val)


def adding(x):
    y = 3
    z = y + x + x
    print(z)
    return z


# adding(4)


# def producing(x):
#     z = x * y
#     return z


# print(producing(adding(4)))

# ============
# You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.


def divide(x):
    return x / 2


def sum(y):
    return divide(y) + 6


print(sum(4))
print(divide(3))
