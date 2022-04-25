'''
줄바꿈 되는 친구를 띄어쓰기로 표현해내고 싶을떄, end=' '활용
'''

N,X = map(int, input().split())
num = list(map(int, input().split()))

for i in num :
    if i < X :
        print(i, end=" ")