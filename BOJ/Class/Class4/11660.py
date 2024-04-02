# 구간 합 구하기 5 / 실버1
# DP

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == 1 and j == 1:
            dp[i][j] = arr[0][0]
        elif i == 1:
            dp[i][j] = dp[i][j-1] + arr[0][j-1] 
        elif j == 1:
            dp[i][j] = dp[i-1][j] + arr[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    si, sj, ei, ej = map(int, input().split())
    print(dp[ei][ej] + dp[si-1][sj-1] - dp[si-1][ej] - dp[ei][sj-1])