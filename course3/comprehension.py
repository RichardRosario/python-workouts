# syntax: [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
# example:
#new_seq = [value * 4 for value in a_list]
# value * 4 -> the transformer expression
# value -> the variable
# a_list -> the sequence

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries',
             'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
# using filter()
# filter_testing = filter(lambda elem: 'w' in elem, lst_check)
# using comprehensions
filter_testing = [elem for elem in lst_check if 'w' in elem]
# print(filter_testing)

# ===========-You can also combine map and filter operations by chaining them together, or with a single list comprehension.
things = [3, 4, 6, 7, 0, 1]
# chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
# print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
# print([x*2 for x in things if x % 2 == 0])

# ================
L = [12, 34, 21, 4, 6, 9, 42]
# normal for loop
lst = []
for x in L:
    if x > 10:
        lst.append(x)
# print(lst)
# using comprehension for loop
lst2 = [x for x in L if x > 10]
# print(lst2)

# ==============Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"}, {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {
    'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
inner_list = tester['info']
# print(inner_list)
compri = [dict['name'] for dict in inner_list]
print(compri)
