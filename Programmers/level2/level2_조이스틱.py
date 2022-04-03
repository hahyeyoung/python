'''
해당문제풀이 tip
1. 상하의 수 구하기(대문자 아스키코드값 활용, min함수를 활용해서 뒤로 갔을 경우 구하기)
2. 좌우의 수 구하기(A를 만났을 경우의 값 구하기)
'''
def solution(name):
    answer = 0
    # 좌우이동 횟수는 길이 - 1
    move = len(name) - 1

    for i, char in enumerate(name):
        # 알파벳 값 빼기, min으로 A부터, Z부터의 값
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        move = min([move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += move
    return answer