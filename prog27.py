#program to get the system time


import time

#time object contains current time
t = time.localtime()


#print the current time
#string represantation time format

currentDT= time.strftime("%H:%M:%D:%Y")
print('current_time=', currentDT)

