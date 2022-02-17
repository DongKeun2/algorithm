# 연속합 2

n = int(input())
lst = list(map(int, input().split()))

result = -1000
dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = lst[0]
dp[1][0] = lst[0]
for i in range(1, n):
    dp[0][i] = max(lst[i], dp[0][i-1] + lst[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + lst[i])
        
for i in range(n):
    result = max(result, dp[0][i], dp[1][i])

print(result)