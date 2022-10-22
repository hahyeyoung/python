def solution(before, after):
    answer = 0
    be = list(before)
    af = list(after)
    be.sort()
    af.sort()
    if be == af:
        answer = 1
    else :
        answer = 0
    return answer