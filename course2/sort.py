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
