def solution(food):
    answer = ''
    word = ''
    for i in range(1,len(food)):
        word += str(i)*(food[i]//2)
    answer = word+'0'+word[::-1]
    return answer