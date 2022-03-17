# 탈주범 검거

# bfs
def sol(R, C):
    global result

    q = [[R, C]]
    while q:
        # d에 현재 위치의 모양 저장
        si, sj = q.pop(0)
        d = arr[si][sj]
        n = vst[si][sj]
        if n >= L:
            return

        # 현재 모양에서 갈 수 있는 지점 ni, nj
        # ni, nj의 모양이 현재 모양과 연결되어 있어야 이동 가능, 가능한 다음 모양의 모음 f
        di, dj, f = direction.get(str(d))
        for c in range(len(di)):
            ni = si + di[c]
            nj = sj + dj[c]
            if 0 <= ni < N and 0 <= nj < M and (arr[ni][nj] != 0 and arr[ni][nj] in f[c]) and vst[ni][nj] == 0:
                vst[ni][nj] = n+1
                result += 1
                q.append([ni, nj])
    return


T = int(input())

# 현재 위치의 모양과 이동 가능한 다음 위치의 모양 저장
direction = {
    '1': ([-1, 1, 0, 0], [0, 0, -1, 1], [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]),
    '2': ([-1, 1], [0, 0], [[1, 2, 5, 6], [1, 2, 4, 7]]),
    '3': ([0, 0], [-1, 1], [[1, 3, 4, 5], [1, 3, 6, 7]]),
    '4': ([-1, 0], [0, 1], [[1, 2, 5, 6], [1, 3, 6, 7]]),
    '5': ([1, 0], [0, 1], [[1, 2, 4, 7], [1, 3, 6, 7]]),
    '6': ([1, 0], [0, -1], [[1, 2, 4, 7], [1, 3, 4, 5]]),
    '7': ([-1, 0], [0, -1], [[1, 2, 5, 6], [1, 3, 4, 5]])
}

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vst = [[0 for _ in range(M)] for _ in range(N)]
    vst[R][C] = 1

    result = 1
    sol(R, C)

    print(f'#{test_case} {result}')