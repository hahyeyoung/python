from collections import Counter
def solution(k, tangerine):
    answer = 0
    test = Counter(tangerine)
    count = test.most_common()
    for i,j in count:
        if k > 0 :
            k -=j
            answer +=1
    return answer