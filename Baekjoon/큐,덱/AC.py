import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    num = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    check = 0
    if n == 0 :
        num = deque()
    for j in p :
        if j == 'R':
            num.reverse()

        elif j == 'D':
            if len(num) == 0:
                check  =1
                break
            else :
                num.popleft()

    if check == 1:
        print('error')
    else :
        print("["+",".join(num)+"]")

### 다른사람풀이
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):

    p = sys.stdin.readline()  # 수행할 함수
    n = int(sys.stdin.readline())  # 배열에 들어있는 수의 개수
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")  # 배열

    queue = deque(arr)  # 덱 생성

    reverse_flag = 0  # R 플래그
    error_flag = 0  # 에러 플래그

    # 배열에 아무것도 없을 때
    if n == 0:
        queue = []

    for cmd in p:
        # "R"일 때 뒤집기 플래그를 1추가
        if cmd == "R":
            reverse_flag += 1
        # "D"일 때 큐에 아무것도 없으면 에러
        elif cmd == "D":
            if len(queue) < 1:
                error_flag = 1
                print("error")
                break
            # 뒤집기가 짝수이면 원래대로 첫 번째에서 빼줌
            else:
                if reverse_flag % 2 == 0:
                    queue.popleft()
                # 홀수이면 뒤에서 빼는게 뒤집에서 빼는 것이랑 같은 원리
                else:
                    queue.pop()

    if error_flag == 0:
        if reverse_flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")

