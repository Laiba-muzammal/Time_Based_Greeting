# Time-based Greeting Program
# This program:
# 1. Gets and shows the current time in hours, minutes, and seconds.
# 2. Checks the current hour to decide what greeting to show:
#    - Before 12 PM: "GOOD MORNING"
#    - Between 12 PM and 6 PM: "GOOD NOON"
#    - After 6 PM: "GOOD NIGHT"

import time
c_time=time.strftime('%H:%M:%S')
print()
H=int(time.strftime('%H'))
if(H<12):
    print("Good Morning!\nThe current time is: ",c_time)
elif (H<18):
    print ("Good Noon!\nThe current time is: ", c_time)
else :
    print("Good Night!\nThe current time is: ", c_time)