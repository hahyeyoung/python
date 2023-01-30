def gcd(a,b):
    while(b!=0):
        n = a%b
        a = b
        b = n
    return a

t = int(input())
num = list(map(int,input().split()))
for i in range(1,t):
    g = gcd(num[0],num[i])
    print('{0}/{1}'.format(num[0]//g,num[i]//g))
