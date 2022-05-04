# 피타고라스 정리 활용 a와 b의 각각의 제곱 = C의 제곱
# 제곱 **2
while True :
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break
    max_num = max(num)
    num.remove(max_num)
    if num[0]**2 + num[1]**2 == max_num**2 :
        print('right')
    else :
        print('wrong')