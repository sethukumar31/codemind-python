t=int(input())
while(t):
    c=0
    n,a,b,k=map(int,input().split())
    if a%b==0:
        c=n//b-n//a
    elif b%a==0:
        c=n//a-n//b
    else:
        c=n//a+n//b-2*(n//(a*b))
    if c>=k:
        print("Win")
    else:
        print("Lose")
    t-=1    
