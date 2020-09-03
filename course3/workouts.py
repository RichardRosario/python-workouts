import json
import requests
a = 20
b = 15
c = 0

# if b > a:
#     a * 2
#     print(a)
# c = c + (a+b)
# print(c)

str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for char in list(str1):
    if char != " ":
        # print(char)
        chars.append(char)
    # chars = chars + char
# print(chars)

# REST API with GET request
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(type(page))
# print(page.text[:150])  # print the first 150 characters
# print(page.url)  # print the url that was fetched
# print("------")
# x = page.json()  # turn page.text into a python object
# print(type(x))
# print("---first item in the list---")
# print(x[0])
# print("---the whole list, pretty printed---")
# print(json.dumps(x, indent=2))  # pretty print the results

# ====================


# def requestURL(baseurl, params={}):
#     # This function accepts a URL path and a params diction as inputs.
#     # It calls requests.get() with those inputs,
#     # and returns the full URL of the data you want to get.
#     req = requests.Request(method='GET', url=baseurl, params=params)
#     prepped = req.prepare()
#     return prepped.url


# print(requestURL(some_base_url, some_params_dictionary))

# def file_lengthy(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1
f = open('D:\python-workouts\workouts\course3\sample.txt.txt', 'r')

line = f.readlines()
sum = 0
lst = []
for lin in line[6:18]:
    lin = lin.split(',')
    sum += float(lin[1])
    lst += [lin[5]]

mean_SP = sum/12
print(mean_SP)
big = lst[0]

for i in range(len(lst)):
    if lst[i] > big:
        big = lst[i]

max_interest = float(big)
print(max_interest)
