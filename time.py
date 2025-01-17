#differnce between for and while loop
import time
def using_for():
    for i in range(5):
        print(i)
        i=i+1
def using_while():
    i=0
    while i<5:
        print(i)
        i=i+1
t1=time.time()
using_for()
t2=time.time()
using_while()
print(time.time()-t1)
print(time.time()-t2)

# simple alarm clock

i=int(input("set the time in seconds"))
time.sleep(i)
print("time is up")

#countdowntimer

facemask=print("facemask") 
boil_egg=print("boil_egg")
rice=print("rice")
i=input("enter the stuff you wanna do ")
if i=="facemask":
    print("facemask is on")
    time.sleep(4)
    print("time is up")
if i=="boil_egg":
    print("eggs are boiling")
    time.sleep(2)
    print("eggs are boiled")
if i=="rice": 
    print("rice is boiling")
    time.sleep(3)
    print("rice is ready")
else:
    print("invalid input")