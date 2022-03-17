# 캐슬 디펜스
# 구현, 그래프이론, 브루트포스, 시뮬레이션

# 시뮬레이션
def sol(board, tot):
    global result

    # 궁수 위치 저장
    achs = []
    for i in range(M):
        if board[N][i] == 2:
            achs.append([N, i])
    
    # 적 잡을때까지 돌림
    while 1:

        # 적 위치
        enms = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    enms.append([i,j])
        
        # 적 다 잡으면 초기화, 리턴
        if enms == []:
            if result < tot:
                result = tot
            return
        
        # 적 제거
        for ach in achs:
            dist = []
            for enm in enms:
                d = abs(ach[0] - enm[0]) + abs(ach[1] - enm[1])
                dist.append(d)
            md = min(dist)
            mi = dist.index(md)
            ei, ej = enms[mi]
            for idx, v in enumerate(dist):
                if v == md:
                    mi = idx
                    eii, ejj = enms[mi]
                    if ejj < ej:
                        ei = eii
                        ej = ejj
                   
            if md <= D:
                if board[ei][ej] == -1:
                    continue
                else:
                    board[ei][ej] = -1
                    tot += 1
            if enms == []:
                if result < tot:
                    result = tot
                return
        
        # 적 위치 이동
        for i in range(N)[::-1]:
            for j in range(M):
                if board[i][j] == 1:
                    board[i][j] = 0
                    ni = i+1
                    nj = j
                    if ni < N:
                        board[ni][nj] = 1

# 궁수 배치
def a(vst, arr):
    if vst.count(2) >= 3:
        board = []
        for i in range(N):
            ar = []
            for j in range(M):
                ar.append(arr[i][j])
            board.append(ar)
        board.append(vst)
        sol(board, 0)
    else:
        for i in range(M):
            if vst[i] == 0:
                vst[i] = 2
                a(vst, arr)
                vst[i] = 0
    return


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

vst = [0 for _ in range(M)]
result = 0
a(vst, arr)

print(result)