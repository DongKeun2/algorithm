# 동전 1

n, k = map(int, input().split())

# 동전 종류
lst = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    for j in range(lst[i], k+1):
        dp[j] += dp[j-lst[i]]

print(dp[k])
