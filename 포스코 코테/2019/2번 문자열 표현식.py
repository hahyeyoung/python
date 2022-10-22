#hihihi ->3(hi), 축약된 표현식이 주어지면 원래의 문자열 출력
exp = input()
num = ''
word = ''
check = 0
for i in exp:
    if i == '(':
        check = 1
    if check == 1 :
        if i != '(' and i!= ')':
            word +=i
    else :
        num += i
print(word*int(num))
