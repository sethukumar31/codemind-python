t1=0
t2=1
nxtrm=t1+t2
p=0
q=0
f=0
n=int(input())
i=3
while i<=n:
    if nxtrm==n:
        print("True")
        f=1
        break
    t1=t2
    t2=nxtrm
    nxtrm=t1+t2
    i+=1
if f==0:
    print("False")