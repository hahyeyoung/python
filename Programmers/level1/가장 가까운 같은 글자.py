def solution(s):
    answer = []
    word = {}
    for i in range(len(s)):
        if s[i] not in word:
            answer.append(-1)
            word[s[i]] = i
        else:
            answer.append(i-word[s[i]])
            word[s[i]] = i
    return answer