'''
1. 리스트로 입력받기
2. 아스키코드활용
3. 대소문자 대문자로 통일
4. 빈도수가 제일 높은 문자 출력
'''

word = input().upper()
word_list = list(set(word))
best = []

for i in word_list :
    cnt = word.count(i)
    best.append(cnt)

if best.count(max(best)) > 1:
    print("?")
else:
    print(word_list[(best.index(max(best)))])
