'''
밖에서 계산해서 넣는것과 안에 직접 넣어서 계산하는 것은
횟수의 차이가 남

'''
def wobaksu(n) :
    if n == 1:
        return print(1)
    elif n%2 == 1:
        wobaksu(3*n+1)
    elif n%2 ==0 :
        wobaksu(n//2)
    print(n)

wobaksu(int(input()))
