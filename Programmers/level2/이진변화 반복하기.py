def solution(s):
    answer = []
    a,b = 0,0
    while(1):
        if s == '1':
            break
        count0 = s.count('0') #0의 개수 세기
        b += count0
        s = s.replace('0','')
        s = bin(len(s))[2:]
        a += 1
    return [a,b]