n=int(input())
m=int(input())
for i in range(1,m+1):
    a,b=map(int,input().split())
    if(a<n or b<n):
        print("UPLOAD ANOTHER")
    elif((a==b) and (a>=n and b>=n)):
        print("ACCEPTED")
    elif(a!=b and (a>=n and b>=n)):
        print("CROP IT")
        