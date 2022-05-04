'''
-> 대각선의 거리는 최소값이 되지 않으므로 고려하지 않음
-> x,y 좌표를 기준으로 w,h까지의 거리와 (0,0) 사이의 거리를 고려해야함
'''

x,y,w,h = map(int, input().split())
print(min(x,y,w-x,h-y))