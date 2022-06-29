# Anytime we start with threads it starts with main thread and any sub threads that you mention are also implemented
# by main thread. Threads can help run the codes on different cores of machine to execute two or more threads
# simultaneously. It depends on how intensive the threads are. Join helps to complete running two threads before
# running the code in main thread

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):   # we use run method because run is defined in multithreading module
        for i in range(5):
            print("Hello")
            sleep(1)   # slow down
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start() # this calls run
sleep(0.2) # prevents collision between threads by un-sinking at different times
t2.start()

t1.join()
t2.join()
# join helps to run threads t1 and t2 before running the remaining part of main thread which is statement "Bye"
print("Bye")
