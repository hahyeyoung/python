T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    result = round((sum(num)- max(num) - min(num))/8)
    print('#%d'%test_case,result)