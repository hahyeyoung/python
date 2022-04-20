'''
stack.append(1) # 삽입 O(1)
stack.pop() # 삭제 O(1)

stack[-1] # 삭제 하지 않고 최상단 원소 가져오기
print(stack) # 최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
'''

from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        time = 0
        for q in queue:
            time += 1
            if price > q:
                break
        answer.append(time)
    return answer