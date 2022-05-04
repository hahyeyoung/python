import math

A,B,V = map(int, input().split())
day = (V-B)/(A-B)
print(math.ceil(day))
'''
1) 시간초과

A,B,V = map(int, input().split())
day = 0
while True:
    V -=A
    day += 1
    if V<A :
        day+=1
        print(day)
        break
    V +=B
'''