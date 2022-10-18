def solution(n, k):
    service =0
    answer = 0
    if n>=10:
        service = n//10
        answer = 12000*n + 2000*(k-service)
    else :
        answer = 12000*n + 2000*k
    return answer