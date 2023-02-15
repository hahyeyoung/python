n, c = map(int, input().split())
things = list(map(int, input().split()))
aw = things[:n//2]
bw = things[n//2:]
asum = []
bsum = []

def bf(wa, suma, l ,w):
    if l >= len(wa):
        suma.append(w)
        return
    bf(wa,suma,l+1,w)
    bf(wa,suma,l+1,w+wa[l])

def bs(arr,target,start,end):
    while start < end :
        mid = (start+end)//2
        if arr[mid]<=target:
            start = mid+1
        else :
            end = mid
    return end

bf(aw, asum ,0,0)
bf(bw, bsum, 0,0)
bsum.sort()

cnt = 0
for i in asum:
    if c-i<0:
        continue
    cnt +=bs(bsum,c-i,0,len(bsum))
print(cnt)