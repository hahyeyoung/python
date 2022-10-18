def solution(my_string, n):
    answer = ''
    word = list(my_string)
    for i in word:
        answer += i*n
    return answer