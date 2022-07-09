n=int(input())
sum=0
f=0
if n<0:
    f=1
    n=abs(n)
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
if f==0:
    print(sum)
else:
    print("-%d" %sum)