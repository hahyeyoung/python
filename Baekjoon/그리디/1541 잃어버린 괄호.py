cal = input().split('-')
result = 0
for i in cal[0].split('+'):
    result += int(i)
for j in cal[1:]:
    for a in j.split('+'):
        result -= int(a)
print(result)