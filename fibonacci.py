t1=0
t2=1
nxtrm=t1+t2
n=int(input())
print("0 1 ",end="")
for i in range(3,n+1,1):
    print(nxtrm,end=" ");
    t1=t2
    t2=nxtrm
    nxtrm=t1+t2