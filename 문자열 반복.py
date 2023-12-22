import sys

cnt=int(input())
for i in range(cnt):
    a,b=map(str,sys.stdin.readline().split())
    for j in range(len(b)):
        print(b[j]*int(a),end="")
    print()
   



