# 적록색약

from collections import deque

# BFS
def sol(si, sj, flag):
    # 적록색약이 아닌사람
    if flag == 0:
        vst1[si][sj] = 1
        q = deque()
        q.append([si, sj])
        c = arr[si][sj]
        while q:
            si, sj = q.popleft()
            for d in range(4):
                ni = si + di[d]
                nj = sj + dj[d]
                if 0 <= ni < N and 0 <= nj < N and vst1[ni][nj] == 0 and arr[ni][nj] == c:
                    vst1[ni][nj] = 1
                    q.append([ni, nj])

    # 적록색약인 사람
    elif flag == 1:
        vst2[si][sj] = 1
        q = deque()
        q.append([si, sj])
        c1 = arr[si][sj]
        if c1 == 'R' or c1 == 'G':
            c1 = 'R'
            c2 = 'G'
        else:
            c2 = 'B'
        while q:
            si, sj = q.popleft()
            for d in range(4):
                ni = si + di[d]
                nj = sj + dj[d]
                if 0 <= ni < N and 0 <= nj < N and vst2[ni][nj] == 0 and (arr[ni][nj] == c1 or arr[ni][nj] == c2) :
                    vst2[ni][nj] = 1
                    q.append([ni, nj])


N = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

arr = [list(input()) for _ in range(N)]
vst1 = [[0 for _ in range(N)] for _ in range(N)]
vst2 = [[0 for _ in range(N)] for _ in range(N)]

cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if vst1[i][j] == 0:
            cnt1 += 1
            sol(i, j, 0)
        if vst2[i][j] == 0:
            cnt2 += 1
            sol(i, j, 1)

print(cnt1, cnt2)