def solution(price, money, count):
    answer = -1
    hap = 0
    for a in range(count+1) :
        hap += a*price
    if hap > money :
        answer = hap-money
    else :
        answer = 0
    return answer