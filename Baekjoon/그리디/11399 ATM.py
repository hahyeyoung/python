#입력받음
m = int(input())
num = list(map(int, input().split()))

#내가 푼 코드
result = 0
mid = 0
num.sort()
for i in num :
    mid = mid+i
    result = result+mid
print(result)

#답을 본 풀이
#result = 0
#num.sort()
#for i in range(m):
   # for j in range(i+1):
  #      result += num[j]
#print(result)

#답지풀이2
#for x in range(1, n+1):
#    answer += sum(peoples[0:x])  # 리스트의 0번째 수부터 x번째 수까지를 더해줍니다.
#print(answer)  # 정답 제출