def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            word = s[i:j]
            if word == word[::-1]:
                answer = max(answer, len(word))
    return answer