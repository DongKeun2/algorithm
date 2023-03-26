# 게임 맵 최단거리 Lv2
# 깊이/너비 우선 탐색(DFS/BFS)

# BFS 풀이
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    vst = [[-1]*m for _ in range(n)]
    q = deque([(0, 0)])
    vst[0][0] = 1
    while q:
        si, sj = q.popleft()
        for d in range(4):
            ei = si + di[d]
            ej = sj + dj[d]
            if 0 <= ei < n and 0 <= ej < m and maps[ei][ej] and vst[ei][ej] == -1:
                vst[ei][ej] = vst[si][sj] + 1
                q.append((ei, ej))

    answer = vst[-1][-1]
    return answer