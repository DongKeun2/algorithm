# 호텔

C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] + [100000]*(C+100)

for a, b in arr:
    for i in range(b, C+101):
        dp[i] = min(dp[i], dp[i-b] + a)

print(min(dp[C:C+101]))