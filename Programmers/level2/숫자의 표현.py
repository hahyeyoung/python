#관련 수학공식을 알고있어야 함
def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n: break
            else: continue
    return answer