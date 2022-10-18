def solution(array):
    answer = []
    answer.append(max(array))
    for i in range(len(array)):
        if max(array) == array[i]:
            answer.append(i)
    return answer