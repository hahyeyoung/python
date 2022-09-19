#정답코드
def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer


#틀린코드, 공백이 확인 되지 않아서 틀림
def solution(s):
    answer = s.split()
    for i in range(len(s)):
        if words[i][0].isnumeric():
            words[i]=words[i].lower()
        else :
            words[i]=words[i].capitalize()
            answer = ' '.join(words)
            return answer