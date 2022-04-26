N = int(input())

for i in range(N):
    result = 0
    sum = 0
    OX = list(input())
    for j in OX:
        if j =='O':
            sum = sum+1
            result+=sum
        else :
            sum = 0
    print(result)