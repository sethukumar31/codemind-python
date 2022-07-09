n = input()
k = ""
j = 0
for i in range(len(n)):
    if(n[i] == "6" and j == 0):
        k+="9"
        j+=1
    else:
        k+= n[i]
print(int(k))