import sys
A,B,C = map(int,sys.stdin.readline().split())


def multi(a, n):
    if n == 1:
        return A % C
    else:
        test = multi(a, n // 2)
        if n % 2 == 0:
            return (test * test) % C
        else:
            return (test * test * A) % C


print(multi(A, B))