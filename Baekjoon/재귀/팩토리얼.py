def fac(N) :
    if N<=1:
        return 1
    return fac(N-1)*N

N = int(input())
print(fac(N))