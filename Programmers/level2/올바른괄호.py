def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else :
            if stack and stack[-1]=='(':
                stack.pop()
            else :
                return False
    if not stack :
        return True
    return False