from collections import deque
import sys

n = int(input())
queue = deque([])
for i in range(n):
    word = sys.stdin.readline().split()
    if word[0] == 'push_front' :
        queue.appendleft(word[1])
    elif word[0] == 'push_back':
        queue.append(word[1])
    elif word[0] == 'pop_front' :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])
            queue.popleft()
    elif word[0] == 'pop_back' :
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
            queue.pop()
    elif word[0] == 'size':
        print(len(queue))
    elif word[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif word[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
