from itertools import combinations
def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        test = sum(i)
        check = 0
        for j in range(2,test):
            if test%j == 0 :
                check =1
        if check == 0:
            answer +=1
    return answer