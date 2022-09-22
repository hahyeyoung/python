import math
def solution(n, k):
    answer = []
    number = [i for i in range(1, n+1)]
    while (n != 0):
        temp = math.factorial(n) // n
        index, k = k//temp, k%temp
        if k == 0:
            answer.append(number.pop(index-1))
        else :
             answer.append(number.pop(index))
        n -= 1
    return answer