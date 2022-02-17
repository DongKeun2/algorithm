# 가장 긴 감소하는 부분 수열

n = int(input())
lst = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    idx = i
    for j in range(i):
        if lst[i] < lst[j] and dp[idx] <= dp[j]:
            idx = j
    if idx == i:
        dp[i] = 1
    else:
        dp[i] = dp[idx] + 1

print(max(dp))