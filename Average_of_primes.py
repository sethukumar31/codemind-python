def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in a:
    if(prime(i)):
        s+=i
        c+=1
print("%.2f"%(s/c))