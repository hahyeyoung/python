def solution(array, height):
    array.sort()
    answer = 0
    for i in array:
        if i>height:
            answer +=1
    return answer