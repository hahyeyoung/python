def solution(bin1, bin2):
    answer = ''
    a = int(bin1,2)
    b = int(bin2,2)
    temp = a+b
    answer = bin(temp)[2:]
    return answer

#다른사람풀이
'''
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
'''