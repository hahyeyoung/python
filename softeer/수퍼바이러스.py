import sys
k, P, N = map(int, input().split())
print(k*pow(P, N*10, int(1e9+7)) % int(1e9+7))