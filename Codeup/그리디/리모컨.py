'''
절대값 함수 abs()
'''
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