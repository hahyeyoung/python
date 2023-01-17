def solution(d, budget):
    answer = 0
    d.sort(reverse=False)
    for i in d:
        if budget-i>=0 :
            budget = budget-i
            answer +=1
    return answer