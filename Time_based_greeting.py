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
