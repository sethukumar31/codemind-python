from math import sqrt
n=int(input())
f=0
for i in range(1,int(sqrt(n)+1)):
    if i*i==n:
        f=1
        print("True")
if f==0:
    print("False")