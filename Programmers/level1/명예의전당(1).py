def solution(k, score):
    answer = []
    tmp = []*k
    for i in score:
        if len(tmp) < k:
            tmp.append(i)
        else :
            if i>= min(tmp) :
                tmp.sort(reverse=True)
                tmp.pop()
                tmp.append(i)
        answer.append(min(tmp))
    return answer