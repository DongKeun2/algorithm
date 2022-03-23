# 수영장

T = int(input())

for test_case in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    lst = list(map(int, input().split()))

    dp = [0 for _ in range(12)]

    dp[0] = min(lst[0]*d, m)
    for i in range(1, 12):
        if i == 11:
            dp[i] = min(dp[i-1]+lst[i]*d, dp[i-1]+m, dp[i-3]+m3, y)
        elif i >= 3:
            dp[i] = min(dp[i-1]+lst[i]*d, dp[i-1]+m, dp[i-3]+m3)
        elif i == 2:
            dp[i] = min(dp[i-1]+lst[i]*d, dp[i-1]+m, m3)
        else:
            dp[i] = min(dp[i-1]+lst[i]*d, dp[i-1]+m)
    
    print(f'#{test_case} {dp[11]}')