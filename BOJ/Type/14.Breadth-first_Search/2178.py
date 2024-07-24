# 미로 탐색
# 그래프이론, 그래프탐색, 너비우선탐색

from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 방문배열 만들어주기 (str => int)
vst = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            vst[i][j] = 1

# 상, 하, 좌, 우
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

# bfs
q = deque()
q.append([0,0])
while q:
    i, j = q.popleft()
    n = vst[i][j]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and vst[ni][nj] == 1:
            vst[ni][nj] = n+1
            q.append([ni, nj])

print(vst[N-1][M-1])