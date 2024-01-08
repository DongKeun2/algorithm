# 쉬운 최단거리 / 실버1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def sol(ni, nj):
    answer[ni][nj] = 0
    q = [(ni, nj)]
    while q:
        si, sj = q.pop(0)
        for d in range(4):
            ei, ej = si + di[d], sj + dj[d]
            if 0 <= ei < N and 0 <= ej < M and arr[ei][ej] == 1 and answer[ei][ej] == -1:
                answer[ei][ej] = answer[si][sj] + 1
                q.append((ei, ej))

answer = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            sol(i, j)

for i in range(N):
    for j in range(M):
        if answer[i][j] == -1:
            if arr[i][j] == 0:
                answer[i][j] = 0
            
for lst in answer:
    print(*lst)