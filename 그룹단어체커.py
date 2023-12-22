cnt=int(input())
hap=0
for i in range(cnt):
    a=input()
    aa=[]
    for j in range(len(a)):
        if a[j] not in aa:
            aa.append(a[j])
        elif a[j] in aa and a[j-1]!=a[j]:
            break
        if j==len(a)-1:
            hap+=1
print(hap)   
