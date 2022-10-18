def solution(cipher, code):
    answer = ''
    word = list(cipher)
    check = 0
    for i in word:
        check +=1
        if check == code:
            answer += i
            check = 0
    return answer

'''
다른사람풀이

def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0:
            answer += cipher[i]
    return answer
'''