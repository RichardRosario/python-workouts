# import turtle
# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

# new_week_temps_f = week_temps_f.split(",")
# sum = 0
# for i in new_week_temps_f:
#     sum += float(i)

# avg_temp = sum / len(new_week_temps_f)
# print(sum)
# print(avg_temp)

# # nums = list(range(0,50))
# # print(nums)

# anna = turtle.Turtle()
# anna.color('orange')
# levi = turtle.Turtle()
# levi.color('violet')
# kobe = turtle.Turtle()
# kobe.color('green')

# for _ in range(15):
#     anna.forward(20)
#     kobe.forward(120)
#     levi.circle(50)
#     anna.left(20)
#     levi.left(60)
#     kobe.left(90)
#     anna.circle(30)
#     levi.forward(40)
#     anna.forward(20)
#     levi.left(40)
#     anna.left(20)

# nums = [94, 45, 100, 78, 16, 5, 79, 86]
#
# large_num = nums[0]
# small_num = nums[0]
#
# for n in nums:
#     if n > large_num:
#         large_num = n
# print(large_num)
#
# for n in nums:
#     if n<small_num:
#         small_num = n
# print(small_num)

# for i in percent_rain:
#     if i > 90:
#         resps.append("Bring an unbrella")
#     elif i >80:
#         resps.append("Good for the flowers?")
#     elif i > 50:
#         resps.append('Watch out for clouds!')
#     else:
#         resps.append("Nice day!")
#
#
# print(resps)
# avg_temp = sum / count
#
# words = ["water", "chair", "pen", "basket", "hi", "car"]
#
# num_words = 0
#
# for i in words:
#     if len(i) > 3:
#         num_words += 1
# print(num_words)

words = ["adopt", "bake", "beam", "confide",
         "grill", "plant", "time", "wave", "wish"]

# past_tense = []
#
# for word in words:
#     if word[-1] == "e":
#         new_word = word + "d"
#     else:
#         new_word = word + "ed"
#     past_tense.append(new_word)
# print(past_tense)

# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# new_rainfall = rainfall_mi.split()
# # rainfall_float = float(new_rainfall)
# print(type(new_rainfall))
#
# num_rainy_months = 0
#
# for i in new_rainfall:
#     if i > '3.0':
#         num_rainy_months += 1
# print(num_rainy_months)
#
# sentence1 = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# sentence_list = sentence1.split()

# # Write your code here.

# same_letter_count = 0

# for word in sentence_list:
#     if word[0] == word[-1]:
#         print(word)
#         same_letter_count += 1
# print(same_letter_count)
# # #
# items = ["whirring", "wow!", "calendar", "wry",
#          "glass", "", "llama", "tumultuous", "owing"]

# acc_num = 0

# for item in items:
#     if "w" in item:
#         acc_num += 1
# print(acc_num)

# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

# new_sentence = sentence.split()
# print(new_sentence)
# num_a_or_e = 0

# for word in new_sentence:
#     if ("a" in word) or ("e" in word) or ("a" and "e" in word):
#         num_a_or_e += 1
# print(num_a_or_e)

# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# vowels = ['a', 'e', 'i', 'o', 'u']

# # Write your code here.
# num_vowels = 0
# for vowel in s:
#     if vowel in vowels:
#         num_vowels += 1

# print(num_vowels)


# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro',
#            'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

# sorted_list = sorted(winners)
# sorted_list.reverse()
# reverse_list = sorted_list

# # z_winners = sorted.reverse()

# print(reverse_list)

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

score = scores.split()

print(score)

a_scores = 0

for i in score:
    if int(i) >= 90:
        a_scores = a_scores+1

print(a_scores)

# stopwords = ['to', 'a', 'for', 'by', 'an',
#              'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# org_lst = org.split()

# acro = ''

# for word in org_lst:
#     if word not in stopwords:
#         acro = acro + word[0].upper()
# print(acro)

# acro = ''

# for word in org_lst:
#     if word not in stopwords:
# acro = acro + (word[0] + word[1]+". ").upper()
# acro = acro + ". ".join(word[0:2].upper())
# acro = '. '.join(word[:2].upper()
#                  for word in org.split() if word not in stopwords)

# print(acro)

p_phrase = "was it a car or a cat I saw"
list_p_phrase = p_phrase.split()

list_p_phrase.reverse()
print(list_p_phrase == p_phrase)

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99",
             "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    name, size, price = item.split(", ")

    print("The store has {} {}, each for {} USD.".format(size, name, price))
