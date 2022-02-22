# 평범한 배낭

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)

for i in range(N):
    for j in range(arr[i][0], K+1)[::-1]:
        dp[j] = max(dp[j], dp[j-arr[i][0]] + arr[i][1])

print(max(dp))
