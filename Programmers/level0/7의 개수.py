def solution(array):
    answer = 0
    for i in array:
        num = i
        while num>0:
            if num%10 == 7:
                answer+=1
                num = num//10
            else :
                num = num//10
    return answer

#다른사람풀이
'''
def solution(array):
    answer = sum([str(i).count("7") for i in array])
    return answer
    

def solution(array):
    return str(array).count('7')

'''