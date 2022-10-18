def solution(num_list, n):
    answer = []
    k = 0
    for i in range(len(num_list)//n):
        answer.append([])
        for j in range(n):
            answer[i].append(num_list[k])
            k+=1
    return answer