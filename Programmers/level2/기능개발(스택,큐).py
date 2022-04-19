'''

'''

def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0

    while len(progresses) > 0:
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer

'''
잘못된 풀이
=> 큐값이 인덱스 값을 벗어남
def solution(progresses, speeds):
    queue = []
    answer = []
    for i in range(0, len(progresses)):
        # 큐에 일수별 저장
        if (100 % speeds[i]) != 0:  # 스피드가 나눠지지 않을 때, 이상일경우 1을 추가로 더함
            k = (100 - progresses[i]) // speeds[i] + 1
            queue.append(k)
        else:
            k = (100 - progresses[i]) // speeds[i]
            queue.append(k)

        if queue[i] > queue[i + 1]:
            cnt += 1
            queue.pop(0)
        else:
            cnt = 1
            queue.pop(0)
        answer.append(cnt)
    return answer

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
solution(progresses, speeds)
'''