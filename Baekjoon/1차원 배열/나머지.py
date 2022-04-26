'''
set() => 중복된 숫자 제거
'''
sum = 0
a = []
for i in range(10):
    N = int(input())
    a.append(N%42)
a = set(a)
print(len(a))