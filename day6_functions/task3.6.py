names=["Joe", "William", "Jack", "Averell"]
final={}
max=0
new_names=[]
for i in names:
    count=len(i)
    if count>max:
        max=count
    final[i]=count
for i in range(max+1):
    for j in final:
        if final[j]==i:
            new_names.append(j)

print(new_names)
print(new_names[::-1])


