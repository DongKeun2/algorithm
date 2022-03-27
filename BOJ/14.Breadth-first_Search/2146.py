# 다리 만들기

from collections import deque

def sol(si, sj, dd):
    global result

    vst = [[0 for _ in range(N)] for _ in range(N)]
    vst[si][sj] = 1
    q = deque([])
    q.append([si, sj])
    while q:
        si, sj = q.popleft()
        n = vst[si][sj]
        if n >= result:
            return
        for d in range(4):
            if d != (dd+2)%4:
                ni = si + di[d]
                nj = sj + dj[d]
                if 0 <= ni < N and 0 <= nj < N and vst[ni][nj] == 0:
                    if arr[ni][nj] == 0:
                        vst[ni][nj] = n+1
                        q.append([ni, nj])
                    elif arr[ni][nj] == 1:
                        if result > n:
                            result = n
                        return


def check(si, sj):
    arr[si][sj] = 2
    q = deque([])
    q.append([si, sj])
    go = [[si, sj]]
    while q:
        si, sj = q.popleft()
        for d in range(4):
            ei = si + di[d]
            ej = sj + dj[d]
            if 0 <= ei < N and 0 <= ej < N and arr[ei][ej] == 1:
                arr[ei][ej] = 2
                q.append([ei, ej])
                go.append([ei, ej])
    
    for i, j in go:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                sol(ni, nj, d)


di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = N*N
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            check(i, j)

print(result)