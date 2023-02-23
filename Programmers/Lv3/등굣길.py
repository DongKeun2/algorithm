# 등굣길 Lv3
# 동적계획법(Dynamic Programming)

# 0으로 초기화, 함정은 -1
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for j, i in puddles:
        dp[i][j] = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not (i == 1 and j == 1): # 해당 길로 올 수 있는 좌, 상 개수 더해주기
                if dp[i][j] == -1:      # 함정은 0으로 바꿔줌
                    dp[i][j] = 0
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    answer = dp[-1][-1] % 1000000007
    return answer