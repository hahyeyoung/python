n = int(input())

for i in range(n):
    H,W,N = map(int,input().split())
    floor = N%H
    ho = N//H+1
    if floor ==0:
        ho -=1
        floor = H
    print(floor*100+ho)

'''
1)틀린코드 : 나머지가 0이 되었을 때의 예외를 처리하지 않음
n = int(input())

for i in range(n):
    H,W,N = map(int,input().split())
    if H > N :
        ho = '01'
        floor = chr(N)
        print(floor+ho)
    else :
        ho = str(N//H+1)
        floor = str(N%H)
        if W >= 10 :
            print(floor + ho)
        else :
            print(floor+'0'+ho)

'''