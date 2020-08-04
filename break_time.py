import webbrowser
from time import sleep

breaks = 3
break_count = 0

while(break_count < breaks):
    sleep(10)
    print(webbrowser.open("https://www.youtube.com/watch?v=EYyarcp5LtU"))
    break_count = break_count + 1
print("promted 3 times")
