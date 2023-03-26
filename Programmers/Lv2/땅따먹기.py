# 땅따먹기 Lv2
# 연습문제

# dp풀이
def solution(land):
    n = len(land)
    m = len(land[0])
    dp = [[0]*m for _ in range(n)]
    for j in range(m):
        dp[0][j] = land[0][j]
    
    for i in range(1, n):
        for j in range(m):
            v = 0
            for k in range(m):
                if j != k and v < dp[i-1][k]:
                    v = dp[i-1][k]
            dp[i][j] = land[i][j] + v
            
    answer = max(dp[-1])
    return answer