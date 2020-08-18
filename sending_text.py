week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
count = 0
for item in week_temps_f:
    count = item + 1

new_week_temps_f = week_temps_f.split(",")
sum = 0

for temp in new_week_temps_f:
    sum = sum + int(temp)

avg_temp = sum / count
