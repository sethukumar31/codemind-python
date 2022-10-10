n=int(input())
ls=[]
for i in range(n):
    p=int(input())
    ls.append(p)
t=int(input())
c=0
for i in ls:
    if i>t:
        c+=2
    else:
        c+=1
print(c)        