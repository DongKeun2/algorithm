# 가장 큰 정사각형 찾기 Lv2
# 연습문제

# dp풀이
# 왼쪽위부터 오른쪽 아래로 탐색
# board의 대각선 왼쪽 위, 위, 왼쪽 값을 확인하여 모두 1이라면
# 해당 칸을 끝으로 만들 수 있는 정사각형의 최대 한 변의 길이 저장 
def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = board[i][j]
            
            elif board[i][j]:
                if board[i-1][j-1] == board[i][j-1] == board[i-1][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 1
    answer = 0
    for i in range(n):
        answer = max(answer, max(dp[i]))
    answer *= answer
    return answer