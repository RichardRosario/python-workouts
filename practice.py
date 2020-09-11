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


# print(sum(4))
# print(divide(3))

# ===== Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

i = 0
accum = 0
while i < len(list1):
    accum = accum + list1[i]
    i += 1
# print(tot)
# print(accum)

# ===== Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


def check_nums(nums):
    new_nums = []
    i = 0
    while i < len(nums):
        if nums[i] != 7:
            break
        new_nums.append(nums[i])
        i += 1
    return new_nums


list = [1, 2, 3, 4, 7, 8, 9]
# print(check_nums(list))

# for n in range(2, 5):
#     if n % 2 == 0:
#         print("Not Weird")
#     elif n % 2 == 1:
#         print('Weird')
# for n in range(6, 20):
#     if n % 2 == 0:
#         print('Weird')
#     elif n > 20:
#         print('Not Weird')

# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}

# print(check[
#     n % 2 == 0 and (
#         n in range(2, 6) or
#         n > 20)
# ])


a = 3
b = 2
c = a+b
d = a-b
e = a*b

# print('{}\n{}\n{}'.format(a+b, a-b, a*b))
