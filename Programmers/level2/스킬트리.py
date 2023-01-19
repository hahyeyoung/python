def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        check = ''
        for j in i :
            if j in skill:
                check +=j
        if skill[:len(check)] == check :
            answer +=1
    return answer