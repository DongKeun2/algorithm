# 스도미노쿠
# 구현, 백트래킹

from itertools import combinations


# n이 보드에 들어갈 수 있는가?
def check(si, sj, n):
    for k in range(9):
        if arr[si][k] == n or arr[k][sj] == n:
            return 0

    ei, ej = 3*(si//3), 3*(sj//3)
    for i in range(ei, ei+3):
        for j in range(ej, ej+3):
            if arr[i][j] == n:
                return 0
    return 1


def sol(cnt):
    global result

    # 스도미노쿠 완성된 상태면 종료(각 실행마다 확인)
    if result:
        return

    # 완성된 상태라면 끝
    if cnt >= 36-N:
        result = arr
        return

    # 왼쪽 상단부터 0인 지점에 조각을 넣을 수 있는 지 확인
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                if i+1 < 9 and arr[i][j] == 0 and arr[i+1][j] == 0:
                    for k in range(len(tmp)):
                        if vst[k] == 0:
                            vst[k] = 1
                            n, m = tmp[k]
                            if check(i,j,n) and check(i+1,j,m):
                                arr[i][j], arr[i+1][j] = n, m
                                sol(cnt+1)
                                if result:
                                    return
                                arr[i][j], arr[i+1][j] = 0, 0
                            if check(i,j,m) and check(i+1,j,n):
                                arr[i][j], arr[i+1][j] = m, n
                                sol(cnt+1)
                                if result:
                                    return
                                arr[i][j], arr[i+1][j] = 0, 0
                            vst[k] = 0

                if j+1 < 9 and arr[i][j] == 0 and arr[i][j+1] == 0:
                    for k in range(len(tmp)):
                        if vst[k] == 0:
                            vst[k] = 1
                            n, m = tmp[k]
                            if check(i,j,n) and check(i,j+1,m):
                                arr[i][j], arr[i][j+1] = n, m
                                sol(cnt+1)
                                if result:
                                    return
                                arr[i][j], arr[i][j+1] = 0, 0
                            if check(i,j,m) and check(i,j+1,n):
                                arr[i][j], arr[i][j+1] = m, n
                                sol(cnt+1)
                                if result:
                                    return
                                arr[i][j], arr[i][j+1] = 0, 0
                            vst[k] = 0
                return


dct ={
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8
}

case = 1
while True:
    N = int(input())
    if N == 0 :
        break
    
    # 게임보드
    arr = [[0 for _ in range(9)] for _ in range(9)]

    # 사용되는 조각모음
    tmp = list(combinations(range(1,10), 2))
    tmp.sort()
    for _ in range(N):
        n1, p1, n2, p2 = input().split()
        arr[dct[p1[0]]][int(p1[1])-1] = int(n1)
        arr[dct[p2[0]]][int(p2[1])-1] = int(n2)
        if n1 > n2:
            n1, n2 = n2, n1
        tmp.remove((int(n1), int(n2)))

    lst = list(input().split())
    for i in range(9):
        arr[dct[lst[i][0]]][int(lst[i][1])-1] = i+1

    # 조각 사용 여부
    vst = [0] * (36-N)
    result = 0
    sol(0)

    print(f'Puzzle {case}')
    if result:
        for i in range(9):
            print(''.join(str(x) for x in result[i]))

    case += 1
