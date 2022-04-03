def solution(x):
    answer = False
    sum = 0
    s = x
    while x>0 :
        sum += int(x%10)
        x = x/10
    print(sum)
    if s%sum ==0 :
        answer = True
    return answer