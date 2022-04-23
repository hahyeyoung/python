'''
어떤 수가 주어졌을 때 생성자가 있다면 가장 작은 생성자를 출력하고, 없다면 0을 출력하면 되는 문제
'''
N = int(input())

for i in range(1,N+1): #분해합의 생성자 찾기
    num = sum((map(int,str(i)))) #i의 각 자리수 더하기
    num_sum = i +num #분해합 = 생성자_각 자리수의 합
    if num_sum ==N:
        print(i)
        break
    if i==N:
        print(0)

'''
1) 잘못된 이해, 잘못된 풀이
분해합의 경우 10으로 나눠서 하나씩 먼저 저장하기
N = int(input())
num = []
num.append(N)

while N!=0: #각각의 자리수별 수 넣기
    a= N%10
    N = N//10
    num.append(a)
'''