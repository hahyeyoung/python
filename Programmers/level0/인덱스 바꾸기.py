def solution(my_string, num1, num2):
    word = list(my_string)
    word[num1],word[num2] = word[num2], word[num1]
    return ''.join(word)