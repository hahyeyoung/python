from collections import deque
n, m = map(int,input().split())
num = list(map(int,input().split()))
queue =deque([i for i in range(1,n+1)])

result = 0

for i in num:
    while True:
        if i == queue[0]:
            queue.popleft()
            break
        else :
            if queue.index(i) <= len(queue)//2:
                queue.rotate(-1)
                result +=1
            else :
                queue.rotate(1)
                result +=1
print(result)