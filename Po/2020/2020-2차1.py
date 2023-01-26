
A = list(map(int, input().split()))
S = int(input())
result = 0

for i in range(len(A)):
    aa = 0
    for j in range(i,len(A)):
        aa += A[j]
        if aa == S:
            result +=1
            break

print(result)