import webbrowser
import time

breaks = 3
break_count = 0

print("program started on: " + time.ctime())
#loop through 3 times
while(break_count < breaks):
    time.sleep(10)
    print(webbrowser.open("https://www.youtube.com/watch?v=EYyarcp5LtU"))
    break_count = break_count + 1

        
print("Last prompt made on: " + time.ctime())
print("Done!")
