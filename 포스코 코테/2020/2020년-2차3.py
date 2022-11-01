b = int(input())
result = 0
for c in range(b,2*b**2):
    for a in range(1,b):
       if b**2 == c**2 - a**2:
           result = c
           break
if result == 0:
    print(-1)
else:
    print(result)


