def solution(operations):
    answer = []
    temp = []
    for i in operations :
        maxnum = 0
        minnum = 0
        if i == 'D 1':
            if not temp:
                continue
            maxnum = max(temp)
            temp.remove(maxnum)
        elif i=='D -1':
            if not temp:
                continue
            minnum = min(temp)
            temp.remove(minnum)
        else:
            a,b = i.split()
            temp.append(int(b))
    if not temp :
        answer = [0,0]
    else :
        answer.append(max(temp))
        answer.append(min(temp))
    return answer