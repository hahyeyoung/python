def solution(my_string):
    answer = ''
    for i in my_string:
        if 65<=ord(i)<97:
            answer += i.lower()
        else :
            answer += i.upper()
    return answer

'''
#다른사람풀이
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer
'''