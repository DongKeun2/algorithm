# 연구소
# 그래프이론, 브루트포스, 그래프탐색, 너비우선탐색

# pypy 통과

from collections import deque

# 바이러스 확산 함수
def bfs(arr):
    global result

    # bfs이용 바이러스 확산
    q = deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append([i, j])
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                q.append([ni, nj])
                arr[ni][nj] = 2

    # 확산 후 안전 영역 크기 갱신
    tot = 0
    for i in range(N):
        tot += arr[i].count(0)
    if result < tot:
        result = tot
    return

# 벽 세우기
def sol(cnt):
    if cnt >= 3:
        arr1 = []
        for i in range(N):
            arr1.append([x for x in arr[i]])
        bfs(arr1)
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    sol(cnt+1)
                    arr[i][j] = 0
        return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
result = 0
sol(cnt)
print(result)