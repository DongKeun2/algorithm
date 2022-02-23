# RGB거리 2

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

result = 1000*N

for i in range(3):
    dp = [[2001,2001,2001] for _ in range(N)]
    dp[0][i] = arr[0][i]

    for j in range(1, N):
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = arr[j][1] + min(dp[j-1][2], dp[j-1][0]) 
        dp[j][2] = arr[j][2] + min(dp[j-1][0], dp[j-1][1])
    
    result = min(result, dp[N-1][(i+1)%3], dp[N-1][(i+2)%3])

print(result)
