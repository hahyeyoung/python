def solution(age):
    answer = []
    age_word = ['a','b','c','d','e','f','g','h','i','j']
    while age>0:
        answer.append(str(age_word[age%10]))
        age = age//10
    answer.reverse()
    return ''.join(answer)

'''
다른사람풀이

def solution(age):
    answer = ''
    age = list(str(age))
    temp = 0

    for i in range(len(age)):
        temp = chr(int(age[i]) + 97)
        answer += temp

    return answer
'''