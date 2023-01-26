N = int(input())
seq = list(map(int,input().split()))
point = 1
answer = 0

for num in seq:
    answer += min(N - abs(point - num), abs(point - num))
    point = num
print(answer)
