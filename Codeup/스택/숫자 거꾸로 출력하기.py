N = int(input())
a = []
if N==0:
    print(0)
while N!=0:
    a.append(N%10)
    N = N//10
print(''.join(map(str,a)))