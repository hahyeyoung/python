n = int(input())
num = list(map(int,input().split()))
num.sort()

left, right = 0, n-1
answer = abs(num[left]+num[right])
final = [num[left],num[right]]
while left<right:
    left_num = num[left]
    right_num = num[right]
    hap = left_num + right_num

    if abs(hap) < answer :
        answer = abs(hap)
        final = [left_num, right_num]
        if answer == 0 :
            break
    if hap<0:
        left +=1
    else :
        right -=1
print(final[0],final[1])
