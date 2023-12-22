aa=[]
hap=0
for i in range(10):
    a=int(input())
    result=a%42
    if result not in aa:
        hap+=1
        aa.append(result)
        
print(hap)
