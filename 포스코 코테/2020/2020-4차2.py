n = int(input())
result = 0
while n>2 :
    if n>=5:
        result += n//5
        n = n % 5
    elif n>=3 :
        result += n//3
        n = n % 3
if n== 1 or n==2 :
    print(-1)
else :
    print(result)
