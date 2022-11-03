'''
#내가푼코드
def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    check = 0
    if sum(works) <n:
        return answer
    else :
        for i in range(1,n+1):
            if check == len(works):
                check = 0
            works[check] = works[check]-1
            check +=1
        for j in works:
            answer += j**2
        return answer
'''

import heapq
def solution(n, works):
    if n >= sum(works):
        return 0

    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)

    return sum([w ** 2 for w in works])