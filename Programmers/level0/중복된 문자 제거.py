def solution(my_string):
    answer = ''
    word = list(my_string)
    for i in word:
        if i not in answer :
            answer +=i
    return answer