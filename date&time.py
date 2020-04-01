'''
#tick
import time

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
'''
import time
import calendar

localtime = time.asctime( time.localtime(time.time()) )
cal = calendar.month(2020, 2)
print (f"Local current time: {localtime} \n")
print ("Here is the calendar:")
print (cal)
