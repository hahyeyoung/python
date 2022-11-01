def solution(emergency):
    answer = []
    temp = emergency.copy()
    temp.sort(reverse=True)
    for i in emergency:
        rank = 1
        for j in temp:
            if i==j:
                answer.append(rank)
            else:
                rank+=1
    return answer