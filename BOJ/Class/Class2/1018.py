# 체스판 다시 칠하기 / 실버 4

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cnt = [[[0] * M for _ in range(N)], [[0] * M for _ in range(N)]]
for i in range(N):
    for j in range(M):
        if (i+j) % 2:
            if arr[i][j] == 'W':
                cnt[0][i][j] = 1
            else:
                cnt[1][i][j] = 1
        else:
            if arr[i][j] == 'B':
                cnt[0][i][j] = 1
            else:
                cnt[1][i][j] = 1

answer = 10**16
for i in range(8, N+1):
    for j in range(8, M+1):
        tmp0 = 0
        tmp1 = 0
        for idx in range(i-8, i):
            tmp0 += sum(cnt[0][idx][j-8:j])
            tmp1 += sum(cnt[1][idx][j-8:j])
        answer = min(answer, tmp0, tmp1)
print(answer)