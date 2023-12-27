# [PCCP 기출문제] 2번 / 석유 시추

# BFS 풀이 
# 각 열의 석유 개수 cnt_list 선언
# 석유가 있는 칸에서 BFS돌면서 idx리스트 생성, cnt_list[idx]에 cnt만큼 추가

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 1 <= len(land) <= 500
def solution(land):
    n = len(land)
    m = len(land[0])
    cnt_list = [0] * m

    def bfs(i, j):
        cnt = 1
        tmp = set([j])
        q = deque([])
        deque.append(q, (i, j))
        while q:
            si, sj = q.pop()
            for d in range(4):
                ei, ej = si + di[d], sj + dj[d]
                if 0 <= ei < n and 0 <= ej < m and land[ei][ej] == 1:
                    if not ej in tmp:
                        tmp.add(ej)
                    cnt += 1
                    land[ei][ej] = 0
                    deque.append(q, (ei, ej))
        for nj in tmp:
            cnt_list[nj] += cnt
        return

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = 0
                bfs(i, j)
    
    answer = max(cnt_list)
    return answer
