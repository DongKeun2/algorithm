# [sw 문제해결 응용] 4일차 - 보급로

# bfs
def sol():
    q = [[0, 0]]
    while q:
        si, sj = q.pop(0)
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]

            if 0 <= ni < N and 0 <= nj < N:
                if cnt[ni][nj] > int(arr[ni][nj]) + cnt[si][sj]:
                    cnt[ni][nj] = int(arr[ni][nj]) + cnt[si][sj]
                    q.append([ni, nj])


T = int(input())

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = [[9*N*N]*N for _ in range(N)]
    cnt[0][0] = 0
    sol()

    print(f'#{test_case} {cnt[N-1][N-1]}')
