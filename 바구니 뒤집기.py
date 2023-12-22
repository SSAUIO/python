import sys

def reverse_list(aa,start,end):
    aa[start-1:end]=reversed(aa[start-1:end])
    return aa

N,M=map(int,sys.stdin.readline().split())
aa=list(range(1,N+1))

for j in range(M):
    a,b=map(int,sys.stdin.readline().split())
    aa=reverse_list(aa,a,b)
    
for k in range(N):
    print(aa[k],end=" ")
