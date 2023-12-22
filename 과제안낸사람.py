aa=[]
bb=[]
for i in range(28):
    aa.append(0)
for j in range(28):
    aa[j]=int(input())

for k in range(1,30):
    if k not in aa:
        bb.append(k)

print(min(bb))
print(max(bb))
        
    
