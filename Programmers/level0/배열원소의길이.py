def solution(strlist):
    answer = []
    word = []
    for i in strlist :
        word.append(list(i))
    for j in word:
        answer.append(len(j))
    return answer