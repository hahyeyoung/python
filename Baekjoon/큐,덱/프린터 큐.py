
t = int(input()) #테스트케이스

for i in range(t):
    n, m = map(int,input().split())
    queue = list(map(int,input().split()))
    idx = list(range(len(queue)))
    idx[m] = 'point'

    result = 0

    while True:
        if queue[0] == max(queue):
            result +=1

            if idx[0] == 'point':
                print(result)
                break
            else :
                queue.pop(0)
                idx.pop(0)
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))


