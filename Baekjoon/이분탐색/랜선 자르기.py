k , n = map(int, input().split())

lensun = []

for i in range(k):
    lensun.append(int(input()))
start, end = 1, max(lensun)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in lensun:
        lines +=i//mid
    if lines >= n:
        start = mid+1
    else:
        end =mid -1
print(end)