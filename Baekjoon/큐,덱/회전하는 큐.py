from collections import deque
n, m = map(int,input().split())
num = list(map(int,input().split()))
queue =deque([i for i in range(1,n+1)])
print(queue)

result = 0
