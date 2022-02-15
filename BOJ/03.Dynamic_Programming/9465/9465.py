# 스티커

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[arr[0][i], arr[1][i]] for i in range(n)]

    dp[1][0] += dp[0][1]
    dp[1][1] += dp[0][0] 
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][1] + dp[i][0], dp[i-2][1] + dp[i][0])
        dp[i][1] = max(dp[i-1][0] + dp[i][1], dp[i-2][0] + dp[i][1])

    result = max(dp[n-1][0], dp[n-1][1])

    print(result)
