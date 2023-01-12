def solution(n):
    answer = 0
    check = 0
    i = 0
    while(check<n):
        i+=1
        answer +=1
        if (i%3==0) or (str(i).find('3')>-1) :
            continue
        else : check+=1
    return answer