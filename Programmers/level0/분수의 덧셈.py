import math
def lcm(a, b):
    return a * b // math.gcd(a, b)
def solution(numer1, denom1, numer2, denom2):
    answer = []
    num= lcm(denom1, denom2)
    a = num//denom1
    b = num//denom2
    c = (numer1*a)+(numer2*b)
    num1 = math.gcd(c,num)
    answer.append(c//num1)
    answer.append(num//num1)
    return answer