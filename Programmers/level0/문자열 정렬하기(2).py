def solution(my_string):
    answer = ''
    word = my_string.lower()
    answer = sorted(word)
    return ''.join(answer)