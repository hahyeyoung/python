def wobaksu(n) :
    print(n)
    if n == 1:
        return 1
    elif n%2 == 1:
        n = 3*n+1
        wobaksu(n)
    else :
        n //= 2
        wobaksu(n)

wobaksu(int(input()))