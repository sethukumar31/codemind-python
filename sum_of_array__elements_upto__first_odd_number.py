n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if(1==(i%2)):
        break
    s+=i
print(s)