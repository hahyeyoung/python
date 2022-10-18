def solution(my_string):
    answer = ''
    word = list(my_string)
    word.reverse()
    for i in word:
        answer +=i
    return answer