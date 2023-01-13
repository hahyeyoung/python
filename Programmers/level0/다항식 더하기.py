def solution(polynomial):
    answer = ''
    x, num = 0, 0
    poly = polynomial.split(' + ')
    for i in poly:
        if i.isnumeric():
            num +=int(i)
        else :
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    if x== 0 and num== 0 :
        answer = ''
    if x== 0 and num!=0:
        answer = str(num)
    if x!=0 and num== 0 :
        if x == 1 :
            answer = 'x'
        else : answer = str(x)+'x'
    if x!=0 and num!=0 :
        if x == 1 :
            answer = 'x'+' + '+str(num)
        else : answer = str(x)+'x'+' + '+str(num)
    return answer