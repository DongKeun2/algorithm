# 재미있는 오셀로 게임

def check():
    global b, w

    for i in range(N):
        b += arr[i].count(1)
        w += arr[i].count(2)


def play(i, j, n):
    for d in range(8):
        for c in range(1, N):
            ni = i + c*di[d]
            nj = j + c*dj[d]
            if c != 1 and 0<=ni<N and 0<=nj<N and arr[ni][nj] == n:
                arr[i][j] = n
                for k in range(1, c):
                    ei = i + k*di[d]
                    ej = j + k*dj[d]
                    arr[ei][ej] = n
                break
            elif 0<=ni<N and 0<=nj<N and arr[ni][nj] == n%2+1:
                continue
            else:
                break


T = int(input())

di = [-1, 1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, -1, 1, 1, -1, 1, -1]

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2, 2
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1

    for _ in range(M):
        i, j, n = map(int, input().split())
        play(i-1, j-1, n)

    b, w = 0, 0
    check()

    print(f'#{test_case} {b} {w}')
