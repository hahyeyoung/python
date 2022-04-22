hour,minu = map(int, input().split())

if minu < 45:
    hour -= 1
    if hour < 0 :
        hour = 24 + hour
    minu = minu+60-45
    print(hour,minu)
else :
    minu -=45
    print(hour, minu)