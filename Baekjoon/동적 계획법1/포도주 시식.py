n = int(input())
grape = []*10000
for i in range(n):
    grape[i].append(int(input()))
d = [0]*10000
d[0] = grape[0]
d[1] = grape[0]+grape[1]
d[2] = max(grape[2]+grape[0], grape[2]+grape[1], d[1])
for i in range(3,n):
    d[i] = max(grape[i]+grape[i-2], grape[i]+grape[i-1]+d[i-3], d[i-1])

print(max(d))
