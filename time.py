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
