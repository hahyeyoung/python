N = int(input())
for i in range (N):
    A, word = input().split()
    text = ''
    for j in word:
        text += int(A)*j
    print(text)

'''
1) 런타임에러
N = int(input())
for i in range (N):
    A, word = input().split()
    A = int(A)
    for j in range(A):
        print(word[j]*A, end='')
        
2) 다른 코드
n = int(input())
for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김
'''