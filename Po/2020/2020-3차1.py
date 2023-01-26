price = int(input())
room = []
for i in range(3):
    a, b = map(int, input().split())
    room.append(price*a+b)

print(room.index(min(room))+1)