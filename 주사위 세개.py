import sys
a,b,c=map(int,sys.stdin.readline().split())

if a==b and b==c and a==c:
    print(a*1000+10000)
elif a==b and a!=c:
    print(a*100+1000)
elif a==c and a!=b:
    print(a*100+1000)
elif b==c and a!=c:
    print(b*100+1000)
else:
    print(max(a,b,c)*100)
    
