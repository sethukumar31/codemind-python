t=int(input())
for i in range(t):
    sum=0
    n=int(input())
    temp=n
    while n!=0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if temp==sum:
        print("True")
    else:
        print("False")