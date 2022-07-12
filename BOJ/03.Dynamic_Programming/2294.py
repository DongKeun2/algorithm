# 동전 2

n, k = map(int, input().split())

# 동전 종류
lst = sorted(list(set([int(input()) for _ in range(n)])))

dp = [10001] * (k+1)
dp[0] = 0
for i in range(len(lst)):
    for j in range(lst[i], k+1):
            dp[j] = min(dp[j], dp[j-lst[i]] + 1)


if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])