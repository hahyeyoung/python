from collections import deque
def solution(A, B):
    answer = 0
    queue = deque(A)
    if A == B :
        return answer
    for i in range(len(queue)):
        answer +=1
        queue.rotate(1)
        if ''.join(queue) == B:
            return answer
        else :
            continue
    if answer == len(queue):
        return -1