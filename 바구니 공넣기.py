import sys
aa=[]
N,M=map(int,sys.stdin.readline().split())
for i in range(N):
    aa.append(0)
for j in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    for k in range(a,b+1):
        aa[k-1]=c
for l in range(N):
    print(aa[l],end=" ")
    
    
