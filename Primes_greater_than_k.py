def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1

n=int(input())
ls=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,n):
    if  ls[i]>=k and prime(ls[i])==1:
        c+=1
print(c)