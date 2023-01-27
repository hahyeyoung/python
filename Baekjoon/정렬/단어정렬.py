n = int(input())
word = []

for i in range(n):
    word_1 = input()
    if word_1 not in word:
        word.append(word_1)

word.sort(key=lambda x : (len(x),x))

for a in word:
    print(a)