def solution(numbers):
    answer = 0
    num = [0,1,2,3,4,5,6,7,8,9]
    numbers.sort()
    for i in num:
        if i not in numbers:
            answer += i
    return answer

'''
다른사람풀이

def solution(numbers):
    return 45 - sum(numbers)
'''