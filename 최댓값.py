list1=[0,0,0,0,0,0,0,0,0]
for i in range(9):
    list1[i]=int(input())
    
print(max(list1))
print(list1.index(max(list1))+1)
