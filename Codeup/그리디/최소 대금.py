'''
소수점 뽑기 print("%.1f" %c)
'''
#입력
pasta1 = int(input())
pasta2 = int(input())
pasta3 = int(input()) ##파스타
ju1 = int(input())
ju2 = int(input()) ##쥬스

##가장 작은 음식값 뽑기
a = min(pasta1, pasta2, pasta3)
b = min(ju1, ju2)

##최소 대금
c = (a+b)*1.1
print("%.1f" %c)