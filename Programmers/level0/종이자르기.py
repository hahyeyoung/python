def solution(M, N):
    if M==1 and N==1 :
        answer= 0
    else :
        answer = (M-1) + (N-1)*M
    return answer