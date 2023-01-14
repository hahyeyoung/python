'''
#실패한 코드
    answer = 0
    lines.sort(key = lambda x:x[0])
    #첫번째 선분과 두번째 선분 비교
    if lines[0][0] == lines[1][0]: # 선분의 앞이 똑같을 경우
        answer += lines[0][1] - lines[0][0]
    else : #같지 않을경우
        if lines[1][0]<lines[0][1] :
            answer += lines[0][1]-lines[1][0]
    print(answer)
    #두번쨰와 세번째 선분 비교
    if lines[1][0] == lines[2][0]: # 선분의 앞이 똑같을 경우
        answer += lines[1][1] - lines[1][0]
    else : #같지 않을경우
        if lines[2][0]<lines[1][1] :
            answer += lines[1][1]-lines[2][0]

    #첫번째랑 세번째가 겹치는 경우


'''

def solution(lines):
    starts = [min(a) for a in lines]
    ends = [max(a) for a in lines]
    starts.sort()
    ends.sort()
    answer = 0
    answer += max(0,ends[0] - starts[1])
    answer += max(0, ends[1] - starts[2])
    answer -= max(0, ends[0] - starts[2])
    return answer
