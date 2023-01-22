import math
def solution(a):
    result = [False for _ in range(len(a))]
    test1, test2 = math.inf, math.inf
    for i in range(len(a)):
        if a[i] < test1:
            test1 = a[i]
            result[i] = True
        if a[-1-i] < test2:
            test2 = a[-1-i]
            result[-1-i] = True
    return sum(result)