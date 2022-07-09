n=int(input())
rev=0
while n:
    d=n%10
    if rev<d:
        rev=d
    n=n//10
print(rev)
