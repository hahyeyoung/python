def solution(left, right):
    answer = 0
    for i in range(left, right+1) : #큰 수
        count = 0
        for a in range(1,i+1) : # 약수 구하기
            if i%a == 0 : #약수
                count +=1 #약수 수 세기
        if count%2 == 0 : # 짝수 홀 수 더하기
            answer +=i
        else :
            answer -=i
    return answer
