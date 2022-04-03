def solution(seoul):
    answer = ''
    for i in seoul :
        if (i == 'Kim') :
            answer = str(seoul.index(i))
    return '김서방은 '+answer+'에 있다'
