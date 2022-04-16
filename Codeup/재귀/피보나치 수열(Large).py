'''
메모이제이션 활용
: 이전의 값을 저장해 놓는 것, 동적 계획법의 핵심

'''
fibo = [0]*201
fibo[1]=1

def fibo_f(n):
    if n == 0 or n==1:
        return n
    if fibo[n] == 0:
        fibo[n] = fibo_f(n-1)+fibo_f(n-2)
    return fibo[n]
def fibonacci(n):
    if n==1:
        return n
    return fibo_f(n)
n = int(input())
print(fibonacci(n)%10009)

#시간초과
'''
def fibo(n):
    if n == 0:
        return 0
    elif n ==1 or n==2 :
        return 1
    else :
        return (fibo(n-1) + fibo(n-2))%10009
n = int(input())
print(fibo(n))
'''