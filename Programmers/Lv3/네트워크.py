# 네트워크 Lv3
# 깊이/너비 우선 탐색(DFS/BFS)

from collections import deque

def solution(n, computers):
    # 시작 지점에서 연결된 네트워크 표시
    def bfs(si):
        q = deque([si])
        while q:
            i = q.popleft()
            for j in range(n):
                if computers[i][j] and vst[j] == 0:
                    q.append(j)
                    vst[j] = 1
    
    
    # 아직 연결되지 않은 네트워크라면 +1, BFS 탐색
    answer = 0
    vst = [0] * n
    for i in range(n):
        if vst[i] == 0:
            vst[i] = 1
            answer += 1
            bfs(i)
    return answer