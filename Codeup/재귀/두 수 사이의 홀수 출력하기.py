##값 반환 return 해주기

a,b = map(int, input().split())

def half(a, b) :
    if a<b:
        half(a,b-1)
    if b%2 == 1 :
        print(b, end=' ')
    else :
        return

half(a,b)