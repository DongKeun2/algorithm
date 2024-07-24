# 이동하기

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

tmp = [[0]*M for _ in range(N)]
tmp[0][0] = arr[0][0]
for i in range(N):
    for j in range(M):
        if i == 0 and j != 0:
            tmp[i][j] = arr[i][j] + tmp[i][j-1]
        elif i != 0 and j == 0:
            tmp[i][j] = arr[i][j] + tmp[i-1][j]
        elif i != 0 and j != 0:
            tmp[i][j] = arr[i][j] + max(tmp[i-1][j],tmp[i][j-1], tmp[i-1][j-1])

print(tmp[N-1][M-1])
