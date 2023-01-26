#입력값 K가 쓰여진 종이컵 인덱스 출력
word = 'akeowujq'
n = input()
for i in range(len(word)):
    if n == word[i]:
        print(i)