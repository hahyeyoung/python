'''
수열 6씩 추가로 커짐
'''
N = int(input())

num = 1

while N>1 :
    N-= 6*num
    num +=1
print(num)

'''
=> 시간초과
N = int(input())

zip = 1
num = 1

if N==1:
    print(1)
else :
    while N>zip :
       zip +=6
       num +=1
print(num)
'''