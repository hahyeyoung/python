'''
1) 분수가 1, 2, 3, 4개씩 증가
2) 홀수일때는 a=숫자, b=1 짝수는 반대
'''

n = int(input())
line = 1

while n>line :
    n -= line
    line +=1
if line%2 == 0: #짝수일 떄
    a = n
    b = line -n +1
else : #홀수
    a = line -n +1
    b = n

print(a,"/",b, sep="")