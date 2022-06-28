t=int(input())
c=0
while t:
    x,y=map(int,input().split())
    for i in range(x,y+1):
        d=i%10
        if d==2 or d==3 or d==9:
            c=c+1
    print(c)
    c=0
    t=t-1       
   