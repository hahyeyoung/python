def solution(my_str, n):
    answer = []
    word = ''
    a = 0
    for i in my_str :
        word += i
        a +=1
        if a % n == 0:
            answer.append(word)
            word = ''
            a = 0
        else :
            continue
    if len(word) < n and word != '' :
        answer.append(word)
    return answer