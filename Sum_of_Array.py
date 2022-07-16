n=int(input())
ls=list(map(int,input().split()))
sum=0
for i in range(len(ls)):
    sum+=ls[i]
print(sum)