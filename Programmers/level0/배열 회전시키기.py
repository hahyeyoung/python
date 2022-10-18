from collections import deque
def solution(numbers, direction):
    answer = []
    num = deque(numbers)
    if direction == 'left':
        num.rotate(-1)
    else :
        num.rotate(1)
    for i in num :
        answer.append(i)
    return answer