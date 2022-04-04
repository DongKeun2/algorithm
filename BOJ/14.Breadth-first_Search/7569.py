# 토마토

from collections import deque
import sys
input = sys.stdin.readline

# 토마토가 다 익었는지 확인
def check():
    global result

    for h in range(H):
        for i in range(N):
            if 0 in arr[h][i]:
                result = -1
                return
            if result < max(vst[h][i]):
                result = max(vst[h][i])


# 해당 토마토가 익은 날 vst에 저장
def sol():
    while q:
        sh, si, sj = q.popleft()
        n = vst[sh][si][sj]
        for d in range(6):
            nh = sh + dh[d]
            ni = si + di[d]
            nj = sj + dj[d]
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0 and  vst[nh][ni][nj] == -1:
                vst[nh][ni][nj] = n+1
                arr[nh][ni][nj] = 2
                q.append([nh, ni, nj])


M, N, H = map(int, input().split())

dh = [-1, 1, 0, 0, 0, 0]
di = [0, 0, -1, 1, 0, 0]
dj = [0, 0, 0, 0, -1, 1]

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
vst = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 익은 토마토 q에 저장, vst에 0으로 저장
q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                vst[h][i][j] = 0
                q.append([h, i, j])
sol()

result = 0
check()

print(result)