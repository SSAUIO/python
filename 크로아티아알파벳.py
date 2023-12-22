while True:
    try:
        a = list(input())
        total = len(a) #일단 전체를 크로아티아 알파벳으로 간주 
        
        for i in range(len(a)-1): #인덱스 범위초과를 막기위해 범위지정
            if a[i] + a[i+1] == "c=" or a[i] + a[i+1] == "c-" or a[i] + a[i+1] == "lj" or \
               a[i] + a[i+1] == "nj" or a[i] + a[i+1] == "s=" or a[i] + a[i+1] == "z=" or \
               a[i] + a[i+1] == "d-":
                total -= 1

        for i in range(len(a)-2):
            if a[i] + a[i+1] + a[i+2] == "dz=":
                total -= 1

        print(total)
    except EOFError:
        break
