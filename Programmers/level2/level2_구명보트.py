def solution(people, limit):
    answer = 0
    people.sort() ##정렬
    i, j = 0, len(people)-1
    while i<=j :
        answer +=1
        if people[i]+people[j] <= limit :
            i +=1
        j -=1
    return answer

''' 실패한 코드 1
def solution(people, limit):
    answer = 0
    people.sort() ##정렬
    a = limit - 40
    for i in people :
        if i > a :
            answer+=1
            b = (len(people) - answer)//2
            c = (len(people) - answer)%2
            answer = answer + b + c
            return answer
'''