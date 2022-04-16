def primid(n) :
    if n != 1:
        primid(n-1)
    print('*' * n)
primid(int(input()))

