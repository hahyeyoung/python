n = int(input())
num = list(map(int,input().split()))

if len(num) == 1:
    result = num[0]*num[0]
else :
    result = max(num)*min(num)
print(result)