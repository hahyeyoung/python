'''
find()함수 해당되는 글자 찾기
'''

word = input()
alphabet = list(range(97, 123)) #아스키 코드 숫자표

for x in alphabet:
    print(word.find(chr(x)), end=' ')

'''
1) 다른 풀이
S = input()
check = [-1]*26
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')
2) 다른풀이
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')
'''




