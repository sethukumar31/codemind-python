n=int(input())
ls=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(len(ls)):
    if i%2==0:
        sum1+=ls[i]
    else:
        sum2+=ls[i]
m=abs(sum1-sum2)
print(m)