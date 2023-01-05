'''
1) 테스트 케이스 시간초과
from itertools import combinations, permutations
def solution(balls, share):
    a = [i for i in range(1, balls+1)]
    answer = len(list(combinations(a, share)))
    return answer
'''

def solution(balls, share):
    a = 1
    b = 1
    c = 1
    for i in range(1,balls+1):
        a *= i
    for j in range(1,(balls-share)+1):
        b *= j
    for k in range(1,share+1):
        c *=k
    answer = a//(b*c)
    return answer

'''
#다른사람 풀이

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
'''