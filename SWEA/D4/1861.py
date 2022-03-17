# 정사각형 방

def sol(si, sj, cnt, sn, n):
    global result, num
    if result < cnt:
        result = cnt
        num = n

    elif result == cnt:
        if num > n:
            num = n

    for d in range(4):
        ni = si + di[d]
        nj = sj + dj[d]
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and (arr[ni][nj] == sn+1):
            v[ni][nj] = 1
            sol(ni, nj, cnt+1, arr[ni][nj], n)
            v[ni][nj] = 0
    return


T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [[0 for _ in range(N)] for _ in range(N)]

    result = 0
    num = N*N
    for i in range(N):
        for j in range(N):
            v[i][j] = 1
            sol(i, j, 1, arr[i][j], arr[i][j])
            v[i][j] = 0

    print(f'#{test_case} {num} {result}')
