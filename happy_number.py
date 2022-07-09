def fun(n):
    s=0
    while n:
        d=n%10
        s+=d*d
        n=n//10
    return s
n=int(input())    
while n>9:
    p=fun(n)
    n=p
if n==1 or n==7:
    print("True")
else:
    print("False")