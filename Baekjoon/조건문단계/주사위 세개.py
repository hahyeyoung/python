a,b,c = map(int, input().split())
if (a == b) and (b == c) :
    sum = 10000+a*1000
    print(sum)
elif (a==b) or (b==c) :
    sum = 1000+b*100
    print(sum)
elif a==c:
    sum = 1000+a*100
    print(sum)
else :
    nummax= max(a,b,c)
    sum = nummax*100
    print(sum)