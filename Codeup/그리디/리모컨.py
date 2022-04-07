'''
절대값 함수 abs()
'''

#입력
a, b = map(int, input().split())
#온도조절 버튼
result = 0
# a>b 또는 a<b 일경우가 있어 절대값으로 구함
c = abs(b-a)
#값 구하기
while c!=0 :
    if c >= 10 :
        c = c-10
        result +=1
    else :
        if c>7:
            c +=1
            result += 1
        elif c>4:
            c = c-5
            result += 1
        elif c >2 :
            c +=1
            result += 1
        else:
            c = c-1
            result += 1
print(result)

'''
*실패한 코드

- 현 풀이의 경우 : 현재온도-목표온도 를 기준으로 계산
=> 현재온도>목표온도인 경우는 성립이 되지만 그 반대의 경우는 성립이 어려움

#입력
a, b = input().split()

#온도조절 버튼
but = [10,5,1]
result = 0

# a>b 또는 a<b 일경우가 있어 절대값으로 구함
c = abs(int(b)-int(a))

#값 구하기
for i in but :
    result += c//i
    c = c%i
print(result)

**실패한 코드 2
#입력
a, b = input().split()
#온도조절 버튼
result = 0
# a>b 또는 a<b 일경우가 있어 절대값으로 구함
c = abs(int(b)-int(a))
#값 구하기
while c!=0 :
    if c > 7 :
        c = abs(c-10)
        result +=1
    elif c <= 7 and c >= 4 :
        c = abs(c-5)
        result += 1
    elif c <3 and c >=1 :
        c = abs(c - 1)
        result += 1
print(result)




'''
