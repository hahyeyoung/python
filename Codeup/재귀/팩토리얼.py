def hap(n):
    if n<=1:
        return 1
    return hap(n-1)*n
print(hap(int(input())))