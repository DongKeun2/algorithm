# 알고스팟

from collections import deque

# bfs
def sol(si, sj):
    q = deque()
    q.append([si, sj])
    vst[si][sj] = 0
    while q:
        si, sj = q.popleft()
        n = vst[si][sj]
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]
            # 해당 지점 vst 값이 -1이면 아직 이동하지 않온 곳 
            if 0 < ni <= M and 0 < nj <= N and vst[ni][nj] == -1:
                # 벽이 없으면 그냥 이동
                if arr[ni][nj] == '0':
                    vst[ni][nj] = n
                    q.appendleft([ni, nj])
                # 벽이 있으면 허물고 이동
                else:
                    vst[ni][nj] = n+1
                    q.append([ni, nj])


N, M = map(int, input().split())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# vst = 해당 지점까지 벽을 허문 횟수 기록
arr = [['0']*(N+2)] + [['0'] + list(input()) + ['0'] for _ in range(M)]  +  [['0']*(N+2)]
vst = [[-1 for _ in range(N+2)] for _ in range(M+2)]

sol(1, 1)

print(vst[M][N])