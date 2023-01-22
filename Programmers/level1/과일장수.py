def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        test = score[i:i+m]
        if len(test)==m:
            answer += m*min(test)
    return answer