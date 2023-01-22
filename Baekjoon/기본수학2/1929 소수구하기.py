# 시간초과
n, m  = map(int,input().split())

for i in range(n,m+1):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
    if check:
        print(i)

#시간초과 안나는 에라토스테네스의 체 활용 => 사용자정의함수 풀이
import sys
M, N = map(int, sys.stdin.readline().split())

def check_prime(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

for i in range(M, N + 1):
    if check_prime(i):
        print(i)