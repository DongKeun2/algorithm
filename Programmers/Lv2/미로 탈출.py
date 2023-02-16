# 연습문제 Lv2

from collections import deque

# 시작지점에서 레버까지 BFS
# 레버에서 출구까지 BFS
# 둘 중 하나라도 -1이라면 탈출 X
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def solution(maps):
    def bfs(si, sj, ei, ej):
        vst = [[-1]*m for _ in range(n)]
        vst[si][sj] = 0
        q = deque([(si, sj)])
        while q:
            ni, nj = q.popleft()
            if ni == ei and nj == ej:
                return vst[ei][ej]
            for d in range(4):
                mi, mj = ni + di[d], nj + dj[d]
                if 0 <= mi < n and 0 <= mj < m and vst[mi][mj] == -1 and maps[mi][mj] != 'X':
                    vst[mi][mj] = vst[ni][nj] + 1
                    q.append((mi, mj))
        return -1
        
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
            elif maps[i][j] == 'L':
                L = i, j
    answer = -1
    a = bfs(S[0], S[1], L[0], L[1])
    b = bfs(L[0], L[1], E[0], E[1])
    if a != -1 and b != -1:
        answer = a+b
    return answer