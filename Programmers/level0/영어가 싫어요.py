def solution(numbers):
    answer = ''
    word = ''
    for i in numbers:
        word += i
        if word == 'one' :
            answer += '1'
            word = ''
        elif word == 'two':
            answer += '2'
            word = ''
        elif word == 'three':
            answer += '3'
            word = ''
        elif word == 'four':
            answer += '4'
            word = ''
        elif word == 'five':
            answer += '5'
            word = ''
        elif word == 'six':
            answer += '6'
            word = ''
        elif word == 'seven':
            answer += '7'
            word = ''
        elif word == 'eight':
            answer += '8'
            word = ''
        elif word == 'nine':
            answer += '9'
            word = ''
        elif word == 'zero':
            answer += '0'
            word = ''
        else :
            continue
    return int(answer)