n=int(input())
rev=0 
c=0
while n:
    d=n%10
    rev=rev*10+d
    c+=1
    n=n//10
if c==10 and rev%10!=0:
    print("Valid")
else:
    print("Invalid")

