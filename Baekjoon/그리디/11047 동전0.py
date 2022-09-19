n, k = map(int, input().split())
coin = []
for i in range(n):
    money = int(input())
    coin.append(money)
coin.sort(reverse=True)

result = 0
for a in coin:
    if k//a == 0:
        continue
    else:
        result += k//a
        k = k%a
print(result)
