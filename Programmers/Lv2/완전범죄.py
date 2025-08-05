# 2025 프로그래머스 코드챌린지 2차 예선

# dp 풀이
def solution(info, n, m):
    # 3차원 배열 생성, 각 사건마다 a,b 조합이 가능한 위치 표시
    dp = [[[0] * m for _ in range(n)] for _ in range(0, len(info) + 1)]
    dp[0][0][0] = 1
    for i in range(1, len(info) + 1):
        for j in range(n):
            for k in range(m):
                if dp[i-1][j][k]:
                    if j + info[i-1][0] < n: dp[i][j+info[i-1][0]][k] = 1
                    if k + info[i-1][1] < m: dp[i][j][k+ info[i-1][1]] = 1
    i = 0
    while i < n:
        for j in range(m):
            if dp[len(info)][i][j]:
                return i
        i += 1
    return -1
   