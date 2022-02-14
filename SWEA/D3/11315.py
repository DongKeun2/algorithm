# 오목 판정

def v(n):
    arr = [input() for _ in range(n)]

    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for d in range(4):
                    ni = i
                    nj = j
                    cnt = 1
                    for k in range(4):
                        ni += di[d]
                        nj += dj[d]
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                            cnt += 1
                            if cnt >= 5:
                                return 'YES'
    else:
        return 'NO'


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = v(N)
    print(f'#{test_case} {result}')
