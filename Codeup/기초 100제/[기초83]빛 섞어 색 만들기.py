'''
빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.
'''
a,b,c = map(int, input().split())

cnt = 0

for i in range(0, a) :
    for j in range(0, b):
        for l in range(0, c):
            print(i, j, l)
            cnt+=1
print(cnt)
