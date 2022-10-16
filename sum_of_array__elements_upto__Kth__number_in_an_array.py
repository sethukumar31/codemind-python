n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
    s+=i
    if(k==i):
        break
print(s)