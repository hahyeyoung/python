def solution(numbers):
    numbers.sort()
    answer = 0
    minus = 0
    for i in numbers :
        if i<0:
            minus += 1
    if minus>=2 :
        answer = max(numbers[0]*numbers[1] , numbers[-1]*numbers[-2])
    else :
        answer = numbers[-1]*numbers[-2]
    return answer

'''
다른사람풀이

def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 
'''