T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P*W
    if R>=W:
        B = Q
    else :
        B = Q+(W-R)*S
    print('#%d'%test_case,min(A,B))