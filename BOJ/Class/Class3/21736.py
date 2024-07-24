# 헌내기는 친구가 필요해, 실버2

from collections import deque

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
vst = [[0]*M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            q.append((i, j))
            vst[i][j] = 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
answer = 0
while q:
    si, sj = q.popleft()
    for d in range(4):
        ei, ej = si + di[d], sj + dj[d]
        if 0 <= ei < N and 0 <= ej < M:
            if not vst[ei][ej] and not arr[ei][ej] == 'X':
                vst[ei][ej] = 1
                q.append((ei, ej))
                if arr[ei][ej] == 'P': answer += 1

print(answer if answer else 'TT')