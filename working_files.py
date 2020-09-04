# Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
first_forty = ""
with open('D:\python-workouts\workouts\course4\sample.txt', 'r') as f:
    first_forty = f.read()[:40]

# Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.


num_lines = sum(
    [1 for i in open("D:\python-workouts\workouts\course4\sample.txt", "r").readlines() if i.strip()])
print(num_lines)
