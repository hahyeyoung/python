from collections import deque #큐 함수
def solution(priorities, location):
    answer = 0
    prior = deque(priorities) #데이터값 리스트에서 큐로 변환
    while prior :
        if location <0:
            location = len(prior)-1
        if prior[0] < max(prior) : #최대값과 비교
            prior.append(prior.popleft()) #뒤로 밀기
            location -= 1 #위치값 뺴기, 뒤로갔으니
        else :
            prior.popleft()
            answer +=1
            if location == 0:
                return answer
            location -=1
    return answer