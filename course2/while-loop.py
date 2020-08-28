# Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
num = 0
eve_nums = []
while num <= 15:
    if num % 2 == 0:
        eve_nums.append(num)
    num = num + 1
# Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.

list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx = idx + 1

# Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.


def stop_at_four(my_list):
    accum_lst = []
    accum_var = 0

    while (accum_var < len(my_list)) and (my_list[accum_var] != 4):
        accum_lst.append(my_list[accum_var])
        accum_var += 1
    return accum_lst


print(stop_at_four([3, 6, 4, 1, 3]))
