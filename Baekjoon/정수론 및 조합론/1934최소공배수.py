def gcd(x, y):  # 최대공약수 구하기
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):  ## 최소공배수 구하기
    result = (x * y) // gcd(x, y)
    return result


t= int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(lcm(a,b))