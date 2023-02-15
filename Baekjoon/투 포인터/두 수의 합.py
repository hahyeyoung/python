n = int(input())
num = list(map(int,input().split()))
num.sort()
hap = int(input())
answer = 0
left, right = 0, n-1
while left < right :
    temp = num[left]+num[right]
    if temp == hap :
        answer +=1
        left +=1
    elif temp < hap :
        left += 1
    else :
        right -=1
print(answer)