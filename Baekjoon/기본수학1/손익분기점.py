A,B,C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)

'''
내가 푼 처음 코드 (while문 활용)
A,B,C = map(int, input().split())
i = 1
while True :
    if A+(i*B) <= i*C :
        print(i+1)
        break
    elif  A+(i*B) > i*C:
        i+=1
    else:
        print(-1)
        break
'''