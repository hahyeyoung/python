hour,minu = map(int, input().split())
plus = int(input())
minu = minu +plus

if minu >=60 : ##분처리
    hour = hour + (minu//60)
    minu = minu%60
    if hour >=24 :
        hour = hour%24
    print(hour,minu)
else :
    if hour >=24 :
        hour = hour%24
    print(hour, minu)
