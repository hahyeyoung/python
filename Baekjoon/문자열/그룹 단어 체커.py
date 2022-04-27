'''
in 함수 그 안에 단어가 있는지 확인하는것
N의 개수에서 해당되지 않는 개수를 뺌

'''
N = int(input())
result = N
for i in range(N):
    word = input()
    for j in range(0,len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -=1
            break

print(result)

'''
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
'''