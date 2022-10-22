
result2 = 0
def fib(n) :
    if (n == 1) or (n == 2) :
        return 1  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2))


def f(n):
    global result2
    dp = [0]*(n+1)
    dp[1],dp[2] = 1,1
    for i in range(3,n+1):
        result2 += 1
        dp[i] = dp[i - 1] + dp[i - 2]  # 코드2
    return result2

n = int(input())
print(fib(n), f(n))