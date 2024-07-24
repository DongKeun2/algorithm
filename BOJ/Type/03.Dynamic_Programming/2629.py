# 양팔저울
# 31444KB, 312ms

N = int(input())
lst = list(map(int, input().split()))

# 참고를 위한 tmp, 기록을 위한 dp
tmp = [0] * 40001
dp = [0] * 40001
for i in range(N):
    dp[lst[i]] = 1
    for j in range(40001):
        if tmp[j] == 1:
            if 0 <= j + lst[i] <= 40000:
                dp[j+lst[i]] = 1
            if 0 <= abs(j-lst[i]) <= 40000:
                dp[abs(j-lst[i])] = 1
    tmp = dp.copy()

M = int(input())
if M:
    mable = list(map(int, input().split()))

    result = []
    for m in mable:
        if dp[m] == 1:
            result.append('Y')
        else:
            result.append('N')

    print(' '.join(result))
