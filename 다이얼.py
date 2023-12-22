a=input()
hap=0
for i in range(len(a)):
    if a[i] in "ABC":
        hap+=3
    elif a[i] in "DEF":
        hap+=4
    elif a[i] in "GHI":
        hap+=5
    elif a[i] in "JKL":
        hap+=6
    elif a[i] in "MNO":
        hap+=7
    elif a[i] in "PQRS":
        hap+=8
    elif a[i] in "TUV":
        hap+=9
    elif a[i]in "WXYZ":
        hap+=10

print(hap)
    
