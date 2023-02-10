import sys
import heapq
n = int(input())
heap = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0 :
        heapq.heappush(heap,(-a))
    else :
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
