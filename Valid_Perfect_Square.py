from math import sqrt
t=int(input())
while t:
    f=0
    n=int(input())
    for i in range(1,int(sqrt(n)+1)):
        if i*i==n:
            f=1
            print("True")
            break
    if f==0:
        print("False")    
    t=t-1