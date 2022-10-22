def solution(i, j, k):
    answer = 0
    for a in range(i,j+1):
        word = list(str(a))
        for b in word:
            if b==str(k):
                answer+=1
    return answer