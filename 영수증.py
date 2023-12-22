import sys
ctotal=0
utotal=int(input())
count=int(input())

for i in range(count):
    a,b=map(int,sys.stdin.readline().split())
    ctotal+=a*b
if utotal==ctotal:
    print('Yes')
else:
    print('No')
    
