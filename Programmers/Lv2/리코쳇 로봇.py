# 리코쳇 로봇 Lv2
# 연습문제

# DFS 풀이 (시간제한이라면 DP로 한 번 더 풀이해보자)
import sys
sys.setrecursionlimit(10**6)
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def solution(board):
    global answer
    def dfs(si, sj, cnt):
        global answer
        vst[si][sj] = cnt

        # 종료 조건
        if cnt >= answer:
            return
        
        # 4방향에 대해 가능한 끝 지점 탐색
        for d in range(4):
            ni = si
            nj = sj
            while True:            
                ni += di[d]
                nj += dj[d]
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                    continue
                
                # 로봇이 도착할 수 있는 지점이 목표지점이면 최소로 갱신
                # 목표 지점이 아니라면 해당 지점에서 한 번 더 DFS탐색
                # 한 번 방문했던 지점이라면 더 적은 이동횟수로 방문할 수 있다면 진행
                else:
                    ni -= di[d]
                    nj -= dj[d]
                    if ni == ei and nj == ej:
                        answer = min(answer, cnt + 1)
                    elif (ni != si or nj != sj) and (vst[ni][nj] == -1 or vst[ni][nj] > cnt + 1):
                        dfs(ni, nj, cnt + 1)
                    break
                    
        
    n = len(board)
    m = len(board[0])
    arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'D':
                arr[i][j] = 1
            elif board[i][j] == 'R':
                si, sj = i, j
            elif board[i][j] == 'G':
                ei, ej = i, j
                
    vst = [[-1]*m for _ in range(n)]
    answer = 10**18
    dfs(si, sj, 0)
    if answer == 10**18:
        answer = -1
    return answer