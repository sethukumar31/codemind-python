n=int(input())
ls=list(map(int,input().split()))
sum=0
for i in range(len(ls)):
    if ls[i]%2==0:
        sum+=ls[i]
print(sum)