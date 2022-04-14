'''
리스트 입력값을 넣을때는 list 함수 활용
'''

n = int(input())
stak = list(map(int,input().split()))
stak.reverse()
print(' '.join(map(str,stak)))
