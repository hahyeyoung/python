text = input()

word = ''
check = 0
for i in range(len(text)-1):
    if text[i].isupper() != text[i+1].isupper():
        if text[i].isupper() == True:
            word += text[i]
            check = 0
    else:
        if text[i].isupper() == True and check == 0:
            word +=text[i]
            check +=1
print(word)
