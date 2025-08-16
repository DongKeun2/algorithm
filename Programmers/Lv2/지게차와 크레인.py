# 2025 프로그래머스 코드챌린지 1차 예선

from collections import deque

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    arr = [[0]*m for _ in range(n)]
    def bfs(target):
        vst = [[0]*m for _ in range(n)]
        q = deque([])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    vst[i][j] = 1
                    q.append((i, j))

        t_lst = []
        while q:
            si, sj = q.pop()
            if arr[si][sj]:
                for d in range(4):
                    ei, ej = si + di[d], sj + dj[d]
                    if 0 <= ei < n and 0 <= ej < m:
                        if not vst[ei][ej]:
                            vst[ei][ej] = 1
                            if arr[ei][ej]: q.append((ei, ej))
                            elif storage[ei][ej] == target: t_lst.append((ei, ej))
            elif storage[si][sj] == target: t_lst.append((si, sj))
        for ti, tj in t_lst: arr[ti][tj] = 1
        

    for s in requests:
        if len(s) == 1: bfs(s[0])
        else:
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == s[0] and not arr[i][j]:
                        arr[i][j] = 1
                        
    answer = 0
    for i in range(n): answer += arr[i].count(0)
    return answer