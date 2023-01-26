#놀이공원 가격 Price 이용횟수 Count, 돈 money
#놀이공원 가격의 총합 이용횟수와 가격을 곱한값

price = int(input())
count = int(input())
money = int(input())

answer = 0
for i in range(1,count+1):
    answer += price*i
if money-answer < 0:
    print(abs(money-answer))
else :
    print(0)