'''
여러 조건들을 순서대로 비교하면서 처리하기 위해서 조건문을 여러 번 중첩할 수 있다.

if 조건식1 :
  ...
else :
  if 조건식2 :
    ...
  else :
    if 조건식3 :
      ...
    else :
      ...
...
if 조건식1 :
  ...
elif 조건식2 :
  ...
elif 조건식3 :
  ...
else :
  ...
도 똑같은 기능을 한다. elif는 else if 의 짧은 약어라고 생각해도 된다.
elif 를 사용하면 if ... else ... 구조를 겹쳐 사용할 때처럼, 여러 번 안 쪽으로 들여쓰기 하지 않아도 된다.


'''
n = int(input())
if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D')