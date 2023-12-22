import sys
aa=[]
N,M=map(int,sys.stdin.readline().split())
for i in range(N):
    aa.append(i+1)
for j in range(M):
    a,b=map(int,sys.stdin.readline().split())
    temp=aa[a-1]
    aa[a-1]=aa[b-1]
    aa[b-1]=temp
   
for k in range(N):
    print(aa[k],end=" ")
