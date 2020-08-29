# sort by last char
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


def last_char(str):
    return str[-1]


nums_sorted = sorted(nums, reverse=True, key=last_char)

# sort by 2nd letter
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']


def second_let(x):
    return x[1]


sorted_by_second_let = sorted(ex_lst, key=second_let)

# sort by last char using lambda
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse=True, key=lambda str: str[-1])

# more sorting
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6,
              "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary)
# reverse
sorted_values = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)


groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3,
             'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

grocery_keys_sorted = sorted(groceries)
