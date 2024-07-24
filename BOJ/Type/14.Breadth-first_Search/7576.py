# 토마토
# 너비우선탐색, 그래프이론, 그래프탐색
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 토마토의 위치 q에 추가시켜주기
q = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i,j])

# 상,하,좌,우 방향 설정
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]


# 토마토 익히기(bfs)
while q:
    i, j = q.popleft()
    n = arr[i][j]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = n+1
            q.append([ni, nj])


# 2이상의 수가 없다면 하루만에 다 익은 것이므로 cnt에 0저장
cnt = 0
for i in range(N):
    # 0이 남아있다면 안 익은 토마토가 있으므로 cnt에 -1 저장
    if cnt == -1:
        break
    for j in range(M):
        if arr[i][j] == 0:
            cnt = -1
            break
        # cnt+1보다 큰 수가 있다면 그 값보다 1작은 값으로 갱신
        elif cnt+1 < arr[i][j]:
            cnt = arr[i][j] -1
print(cnt)