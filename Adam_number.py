n=int(input())
temp=n
p=temp*temp
rev=0
while(n):
    d=n%10
    rev=rev*10+d
    n=n//10
q=rev*rev
rev=0
t=q
while(q):
    d=q%10
    rev=rev*10+d
    q=q//10
if(rev==p):
    print("True")
else:
    print("False")
    