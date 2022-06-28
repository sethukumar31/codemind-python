a,b,c=map(int,input().split())
if a>50 and b>60 and c>100:
    g=10
elif a>50 and b>60:
    g=9
elif b>60 and c>100:
    g=8
elif a>50 and c>100:
    g=7
elif a>50 or b>60 or c>100:
    g=6
else:
    g=5
print(g)