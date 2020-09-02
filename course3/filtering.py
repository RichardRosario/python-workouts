# normal or long method of filtering data
# def keep_evens(nums):
#     new_list = []
#     for num in nums:
#         if num % 2 == 0:
#             new_list.append(num)
#     return new_list

# print(keep_evens([3, 4, 6, 7, 0, 1]))


# using filer() method
def keep_evens(nums):
    new_list = filter(lambda num: num % 2 == 0, nums)
    return new_list


# print(keep_evens([3, 4, 6, 7, 0, 1]))
# ============
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries',
             'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = filter(lambda elem: 'w' in elem, lst_check)

print(list(filter_testing))

# =============
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = filter(lambda word: 'o' in word, lst)

print(list(lst2))
