#입력
money = int(input())

#거스름돈
coins = [50000,10000,5000,1000,500,100,50,10]
coin = 0
#거슬러주기
for i in coins:
    coin += money//i ##제시된 금액을 거스름돈으로 나누기
    money = money%i  ##머니에는 나머지 금액넣기

print(coin)