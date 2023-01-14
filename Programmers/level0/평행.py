from itertools import combinations
def slopee(x1,y1,x2,y2):
    x = (y2 - y1) / (x2 - x1)
    return x

def solution(dots):
    answer = 0
    lines = []
    for a,b in combinations(dots,2):
        cnt = slopee(a[0],a[1],b[0],b[1])
        if cnt not in lines :
            lines.append(cnt)
        else :
            answer = 1
    return answer