# 러시아 국기 같은 깃발

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    dp = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        dp[i][0] = M - arr[i].count('W')
        dp[i][1] = M - arr[i].count('B')
        dp[i][2] = M - arr[i].count('R')
    
    result = dp[0][0] + dp[N-1][2]

    dp[1][2] = N*M
    dp[N-2][0] = N*M
    for i in range(2, N-1):
        dp[i][0] += dp[i-1][0]
        dp[i][1] += min(dp[i-1][0], dp[i-1][1])
        dp[i][2] += min(dp[i-1][1], dp[i-1][2])
    
    result += min(dp[N-2])

    print(f'#{test_case} {result}')
