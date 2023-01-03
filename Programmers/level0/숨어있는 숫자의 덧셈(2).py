'''
- "\d+" : 숫자 묶음 단위 별로 추출
- "\d" : 한자리 숫자 단위 별로 추출
'''
import re
def solution(my_string):
    answer = 0
    numbers = re.findall('\d+', my_string)
    for i in numbers:
        answer += int(i)
    return answer