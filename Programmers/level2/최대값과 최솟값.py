def solution(s):
    word = list(map(int, s.split()))
    maxnum = max(word)
    minnum = min(word)
    answer = str(minnum)+' '+str(maxnum)
    return answer