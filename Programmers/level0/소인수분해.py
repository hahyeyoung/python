def solution(n):
    answer = []
    a = 2
    while n>1 :
        if n%a == 0:
            if a not in answer :
                answer.append(a)
            n = n//a
            a = 2
        else :
            a += 1
    return answer
