
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(prev_chars):
    for i in punctuation_chars:
        prev_chars = str(prev_chars).replace('%s' % i, '')
    return prev_chars

# get the positive reactions


def get_pos(str):
    count = 0
    words = str.split()
    for word in words:
        word = strip_punctuation(word)
        if word in positive_words:
            count += 1
    return count

# get the negative reactions


def get_neg(str):
    str = strip_punctuation(str).split()
    count = 0
    for item in str:
        if item in negative_words:
            count += 1
    return count


# open the file with write permission useing "w"
outfile = open("resulting_data.csv", "w")
# write the header of each column
outfile.write(
    "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')

# open the data file
fileconnection = open("project_twitter_data.csv", 'r')

lines = fileconnection.readlines()
print(lines)
header = lines[0]
field_names = header.strip().split(',')
print(field_names)

for row in lines[1:]:

    value = row.strip().split(',')
    # format the string using .format()
    row_string = '{},{},{},{},{}'.format(value[1], value[2], get_pos(
        # get the total response by subtracting negative from positive values
        value[0]), get_neg(value[0]), get_pos(value[0])-get_neg(value[0]))
    outfile.write(row_string)
    outfile.write('\n')

# close and save the file
outfile.close()
