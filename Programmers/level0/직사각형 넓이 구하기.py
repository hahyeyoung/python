def solution(dots):
    dots.sort(key = lambda x :(x[0],x[1]))
    answer = abs((dots[1][1] - dots[0][1]) * (dots[3][0] - dots[0][0]))
    return answer

'''
다른사람풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
'''