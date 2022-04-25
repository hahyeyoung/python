'''
값이 더이상입력되지 않을 때 정지할 때는 try except 구문활용
'''
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
