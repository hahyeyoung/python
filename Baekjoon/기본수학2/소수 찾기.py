N = int(input())
num = list(map(int, input().split()))

for i in num:
    sum = 0
    if i!=1 :
        check = True
    for j in range(2, i):
        if i % j == 0 :
            check = False
            break
        if check :
            sum += 1
print(sum)