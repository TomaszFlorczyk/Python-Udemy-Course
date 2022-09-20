<<<<<<< HEAD
import _thread, time
from concurrent.futures import thread

def printTime( threadName, sleepTime):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()

        print(threadName, time.strftime( "%H %M %S", localTime))
        time.sleep( sleepTime)

        num += 1
    print(threadName, " ended")

_thread.start_new_thread(printTime, ("thread 1", 0.5))
_thread.start_new_thread(printTime, ("Thread 2", 0.3))

=======
import _thread, time
from concurrent.futures import thread

def printTime( threadName, sleepTime):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()

        print(threadName, time.strftime( "%H %M %S", localTime))
        time.sleep( sleepTime)

        num += 1
    print(threadName, " ended")

_thread.start_new_thread(printTime, ("thread 1", 0.5))
_thread.start_new_thread(printTime, ("Thread 2", 0.3))

>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
time.sleep(4)