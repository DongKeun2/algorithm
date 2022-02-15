# sw문제해결 기본 2일차
# Ladder1

T = 10

for _ in range(T):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [1, 0, 0]
    dj = [0, 1, -1]
    result = -1
    for i in range(100):
        if result != -1:
            break
        d = 0
        ni = 0
        nj = i
        if arr[0][i] == 1:
            while ni < 99 and 0 <= nj < 100:
                ni += di[d]
                nj += dj[d]
                if d == 0:
                    if nj + 1 < 100 and arr[ni][nj+1] == 1:
                        d = 1
                    elif nj - 1 >= 0 and arr[ni][nj-1] == 1:
                        d = 2
                else:
                    if nj < 0 or nj >= 100 or arr[ni][nj] == 0:
                        ni -= di[d]
                        nj -= dj[d]
                        d = 0
                if arr[ni][nj] == 2:
                    result = i
                    break

    print(f'#{test_case} {result}')
    