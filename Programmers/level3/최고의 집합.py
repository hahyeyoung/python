def solution(n, s):
    answer = []

    if s < n :
        return [-1]

    for _ in range(n):
        answer.append(s//n)

    indexs = len(answer)-1

    for i in range(s - sum(answer)):
        answer[indexs] += 1
        indexs -= 1

    return answer

##다른사람풀이
'''
def bestSet(n, s):
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n

    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer
'''