from math import pow
n=int(input())
c=0
t=n*n
p1=n
p2=t
while(p1%10):
    c+=1;
    p1//=10
x=(pow(10,c))
if t%x==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
