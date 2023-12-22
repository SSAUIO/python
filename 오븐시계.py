import sys
H,M=map(int,sys.stdin.readline().split())
T=int(input())
H1=(M+T)//60
M2=(M+T)%60

if H+H1>23:
    print(H+H1-24,M2)
else:
    print(H+H1,M2)

