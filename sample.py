# import turtle
# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
#
# new_week_temps_f = week_temps_f.split(",")
# sum = 0
# for i in new_week_temps_f:
#     sum += float(i)
#
# avg_temp = sum / len(new_week_temps_f)
# print(sum)
# print(avg_temp)
#
# # nums = list(range(0,50))
# # print(nums)
#
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
#avg_temp = sum / count
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
#
# sentence_list = sentence1.split()

# Write your code here.

# same_letter_count = 0
#
# for word in sentence_list:
#     if word[0] == word[-1]:
#         print(word)
#         same_letter_count += 1
# print(same_letter_count)
# # #
# items = ["whirring", "wow!", "calendar", "wry",
#          "glass", "", "llama", "tumultuous", "owing"]
#
# acc_num = 0
#
# for item in items:
#     if "w" in item:
#         acc_num += 1
# print(acc_num)
#
# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
#
# new_sentence = sentence.split()
# print(new_sentence)
# num_a_or_e = 0
#
# for word in new_sentence:
#     if ("a" in word) or ("e" in word) or ("a" and "e" in word):
#         num_a_or_e += 1
# print(num_a_or_e)
#
# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# vowels = ['a', 'e', 'i', 'o', 'u']

# Write your code here.
# num_vowels = 0
# for vowel in s:
#     if vowel in vowels:
#         num_vowels += 1
#
# print(num_vowels)
#
# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
#
# score = scores.split()
#
# print(score)
#
# a_scores = 0
#
# for i in score:
#     if int(i) >= 90:
#         a_scores = a_scores+1
#
# print(a_scores)
#
# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro',
#            'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
#
# sorted_list = sorted(winners)
# sorted_list.reverse()
# reverse_list = sorted_list
#
# # z_winners = sorted.reverse()
#
# print(reverse_list)


# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
#
# sports.remove("cricket")
#
# print(sports)

# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
#
#
# winners.reverse()
#
# z_winners = winners
# print(z_winners)

# alist = [4,2,8,6,5]
# blist = [ ]
# for item in alist:
#    blist.append(item+5)
# print(blist)
# lst= [3,0,9,4,1,7]
# new_list=[]
# for i in range(len(lst)):
#    new_list.append(lst[i]+5)
# print(new_list)

# verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
#
# ing = []
#
# for word in verbs:
#     ing.append(word + "ing")
# print(ing)
# numbs = [5, 10, 15, 20, 25]
#
# for i in numbs:
#     num = i+5
#     numbs.append(num)
# del numbs[0:5]
# print(numbs)
#
# wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
#
# past_wrds = []
#
# for wrd in wrds:
#     past_wrds.append(wrd + 'ed')
#
# print(past_wrds)

# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# new_scores = scores.split()

# a_scores = 0
#
# for score in new_scores:
#     if int(score) >= 90:
#         a_score = a_scores+1
#
# print(a_score)
#
# fileref = open("sample.txt", 'r')
# lines = fileref.readlines()
#
# # for line in lines[:4]:
# #     print(line.strip())
# print(len(lines))

# file_write = open("sample.txt", "w")
#
# for num in range(10):
#     square = num * num
#     file_write.write(str(square))
#     file_write.write('\n')
# file_write.close()

# with open("sample.txt", "r") as sample:
#
#     for line in sample:
#         print(line)
# sample = open('sample.txt', "r").read()
#
# num = len(sample)
# print(num)

sample = open('sample.txt', "r").read()

#words = sample.split()
# num_words = 0
#
# for word in words:
#     num_words += 1
# print(num_words)

# three = []
#
# for line in sample:
#    line = line.split()
#    print(line)
#    three += [line[2]]

# print(three)

# words = sample.split()
# p_words = []
#
# for word in words:
#     if "p" in word:
#         p_words.append(word)
# print(p_words)
#
# swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
#
# swimmers['Phelps'] = swimmers['Phelps'] + 5
#
# a = 10
#
# def foo():
#     a = a + 10
# foo()
# print(a)
#
# #Python3 level 2-week2

# --1
# Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
# credits = 0
# for v in Junior:
#     credits = credits + Junior[v]
# print(credits)

# --2
# str1 = "peter piper picked a peck of pickled peppers"
#
# freq ={}
#
# for char in str1:
#     if char not in freq:
#         freq[char] = 0
#     freq[char] = freq[char] + 1

# --3
# s1 = "hello"
#
# counts = {}
#
# for i in s1:
#     if i not in counts:
#         counts[i] = 0
#     counts[i] = counts[i] + 1

# --4
# str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
#
# words = str1.split()
#
# freq_words = {}
#
# for word in words:
#     if word not in freq_words:
#         freq_words[word] = 0
#     freq_words[word] = freq_words[word] + 1

# --5
# sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
# words = sent.split()
#
# wrd_d = {}
#
# for word in words:
#     if word not in wrd_d:
#         wrd_d[word] = 0
#     wrd_d[word] = wrd_d[word] + 1

# --6
# sally = "sally sells sea shells by the sea shore"
#
# characters = {}
#
# for char in sally:
#     if char not in characters:
#         characters[char] = 0
#     characters[char] = characters[char] + 1
#
# keys = list(characters.keys())
# best_char = keys[0]
#
# for key in keys:
#     if characters[key] > characters[best_char]:
#         best_char = key
#--7

# sally = "sally sells sea shells by the sea shore and by the road"
#
# characters = {}
#
# for i in sally:
#     if i not in characters:
#         characters[i] = 0
#     characters[i] = characters[i] + 1
#
# keys = list(characters.keys())
# worst_char = keys[0]
#
# for key in keys:
#     if characters[key] < characters[worst_char]:
#         worst_char = key
#---8
# string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
#
# letter_counts = {}
#
# for letter in string1:
#     letter = letter.lower()
#     if letter not in letter_counts:
#         letter_counts[letter] = 0
#
#     letter_counts[letter] = letter_counts[letter] + 1
#--9
# p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
#
# low_d = {}
#
# for char in p:
#     char = char.lower()
#     if char not in low_d:
#         low_d[char] = 0
#     low_d[char] = low_d[char] + 1
# print(low_d)

# using zip
names = ["Peter","Clark","Wade", "Bruce"]
heroes = ['Spiderman', 'Superman','Deadpool','Batrman']

for name,hero in zip(names,heroes):
    print(f'{name} is {hero}')