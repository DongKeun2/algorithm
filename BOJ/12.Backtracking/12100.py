# 2048 (Easy)
# 구현, 브루트포스, 시뮬레이션, 백트래킹

import copy


# 5번 옮기고 난 뒤 최댓값
def check(arr):
    global result

    mv = 0
    for i in range(N):
        mv = max(mv, max(arr[i]))

    if result < mv:
        result = mv


# d방향으로 옮기기
def move(tmp, d):
    # 한 번 겹쳐진 수는 또 겹쳐질 수 없다.
    vsted = copy.deepcopy(vst)
    # 상
    if d == 0:
        for i in range(1, N):
            for j in range(N):
                if tmp[i][j] != 0:
                    for c in range(0, i)[::-1]:
                        if tmp[c][j] == 0:
                            tmp[c][j] = tmp[c+1][j] 
                            tmp[c+1][j] = 0
                        else:
                            if tmp[c][j] == tmp[c+1][j] and vsted[c][j] == 0:
                                tmp[c][j] *= 2
                                tmp[c+1][j] = 0
                                vsted[c][j] = 1
                            break
    # 하
    elif d == 1:
        for i in range(0, N-1)[::-1]:
            for j in range(N):
                if tmp[i][j] != 0:
                    for c in range(i+1, N):
                        if tmp[c][j] == 0:
                            tmp[c][j] = tmp[c-1][j] 
                            tmp[c-1][j] = 0
                        else:
                            if tmp[c][j] == tmp[c-1][j] and vsted[c][j] == 0:
                                tmp[c][j] *= 2
                                tmp[c-1][j] = 0
                                vsted[c][j] = 1
                            break
    # 좌
    elif d == 2:
        for j in range(1, N):
            for i in range(N):
                if tmp[i][j] != 0:
                    for c in range(0, j)[::-1]:
                        if tmp[i][c] == 0:
                            tmp[i][c] = tmp[i][c+1]
                            tmp[i][c+1] = 0
                        else:
                            if tmp[i][c] == tmp[i][c+1] and vsted[i][c] == 0:
                                tmp[i][c] *= 2
                                tmp[i][c+1] = 0
                                vsted[i][c] = 1
                            break
    # 우
    else:
        for j in range(0, N-1)[::-1]:
            for i in range(N):
                if tmp[i][j] != 0:
                    for c in range(j+1, N):
                        if tmp[i][c] == 0:
                            tmp[i][c] = tmp[i][c-1]
                            tmp[i][c-1] = 0
                        else:
                            if tmp[i][c] == tmp[i][c-1] and vsted[i][c] == 0:
                                tmp[i][c] *= 2
                                tmp[i][c-1] = 0
                                vsted[i][c] = 1
                            break
    return tmp


# 현 상태에서 상, 하, 좌, 우로 이동
def sol(arr, cnt):
    global result

    # 5번 이동 후 검사
    if cnt == 5:
        check(arr)
        return

    # 이미 구한 결과가 나올 수 있는 최댓값인 경우
    if result >= ms:
        return

    if cnt > 5:
        return
    
    # 상, 하, 좌, 우로 이동한 뒤 cnt 증가
    for d in range(4):
        tmp = copy.deepcopy(arr)
        sol(move(tmp, d), cnt+1)


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
vst = [[0 for _ in range(N)] for _ in range(N)]

# 혹시 모를 간단한 백트래킹
ms = 0
for i in range(N):
    ms += sum(board[i])

result = 2
sol(board, 0)

print(result)