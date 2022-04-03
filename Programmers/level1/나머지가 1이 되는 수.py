def solution(n):
    answer = 1
    for answer in range(n) :
        answer = answer+1
        if (n%answer) == 1 :
            return answer
