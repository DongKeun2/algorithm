# 단지번호붙이기

from collections import deque

def sol(si, sj):
    q = deque()
    q.append([si, sj])
    cnt = 1
    while q:
        si, sj = q.popleft()
        for d in range(4):
            ni, nj = si+di[d], sj+dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1':
                arr[ni][nj] = '0'
                q.append([ni, nj])
                cnt += 1
    result.append(cnt)
    return


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
arr = [list(input()) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            arr[i][j] = '0'
            sol(i, j)

result.sort()
print(len(result))
for x in result:
    print(x)