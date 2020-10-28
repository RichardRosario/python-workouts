import csv
from datetime import datetime
# Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
path = "D:\python-workouts\workouts\AAL_data.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
# print(header)
data = []
for row in reader:
    #row = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
    date = datetime.strptime(row[0], '%Y-%m-%d')
    open_price = float(row[1])
    high_price = float(row[2])
    low_price = float(row[3])
    close_price = float(row[4])
    trade_vol = int(row[5])
    name = str(row[6])
    data.append([date, open_price, high_price,
                 low_price, close_price, trade_vol, name])

# compute and store daily returns
returns_path = "D:\python-workouts\workouts\AAL_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(['Date', "Return"])

# iterate through the data
for i in range(len(data)-1):
    todays_row = data[i]
    # print(todays_row)
    todays_date = todays_row[0]
    todays_price = todays_row[1]
    yesterday_row = data[i+1]
    yesterday_price = yesterday_row[1]

    daily_return = (todays_price - yesterday_price) / yesterday_price
    # writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
    # print("Date: {}, Daily ROI: {}".format(formatted_date, daily_return))


# Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.


# num_lines = sum(
#     [1 for i in open("D:\python-workouts\workouts\course4\sample.txt", "r").readlines() if i.strip()])
# print(num_lines)
# find number of characters in a file
f = open("D:\python-workouts\workouts\AAL_returns.csv", "r")

data = f.read().replace(" ", "")
# print(data)
num_chars = len(data)
# print("There are {} of characters in this file!".format(num_chars))


line = open('SP500.txt', 'r').readlines()
# print(line)

sum = 0
list = []

for lin in line[6:18]:
    lin = lin.split(',')

    sum += float(lin[1])

    list += [lin[5]]

mean_SP = sum/12
# print(mean_SP)

interest = list[0]

for i in range(len(list)):
    if list[i] > interest:
        interest = list[i]

max_interest = float(interest)

print(max_interest)
