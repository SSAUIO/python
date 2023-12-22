piece = [1,1,2,2,2,8]
input = list(map(int, input().split()))
output = []
for i in range(6):
    num = (piece[i] - input[i])
    output.append(num)
    print(output[i], end=' ')

        
