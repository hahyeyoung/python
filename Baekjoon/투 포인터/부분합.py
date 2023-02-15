n, hap = map(int,input().split())
num = list(map(int,input().split()))

target = 0
left, right = 0, 0
answer = 1e9

while True :
    if target >= hap :
        answer = min(answer, right-left)
        target -= num[left]
        left +=1
    else :
        if right == n:
            break
        target +=num[right]
        right +=1
print(0) if answer == 1e9 else print(answer)

