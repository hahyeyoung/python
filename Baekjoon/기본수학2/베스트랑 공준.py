def check_prime(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
result = 0
while True:
    n = int(input())
    result = 0
    if n == 0:
        break
    else:
        for i in range(n+1, (2*n)+1):
            if check_prime(i):
                result +=1
        print(result)
