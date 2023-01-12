import fractions
def solution(a, b):
    answer = 1
    num = fractions.gcd(a, b)
    b = b//num
    num = 2
    check1 = 0
    check2 = 0
    while num <= b:
        if b % num == 0:
            if num == 2 or num == 5:
                check1 +=1
            else : check2 +=1
            b = b / num
        else:
            num = num + 1
    if check2 != 0:
        answer = 2
    return answer