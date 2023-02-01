N, M = map(int, input().split())

def count_num(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_num(N, 5) - count_num(M, 5) - count_num(N - M, 5)
two_count = count_num(N, 2) - count_num(M, 2) - count_num(N - M, 2)

answer = min(five_count, two_count)
print(answer)