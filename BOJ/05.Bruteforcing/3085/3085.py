# 사탕 게임
# pypy

N = int(input())

arr = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        if i+1 < N:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            for m in range(N):
                cnt1 = 1
                cnt2 =1
                for n in range(1,N):
                    if arr[m][n] == arr[m][n-1]:
                        cnt1 += 1
                    else:
                        if result < cnt1:
                            result = cnt1
                        cnt1 = 1
                    if arr[n][m] == arr[n-1][m]:
                        cnt2 += 1
                    else:
                        if result < cnt2:
                            result = cnt2
                        cnt2 = 1
                if result < cnt1:
                    result = cnt1
                if result < cnt2:
                    result = cnt2
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

        if j+1 < N:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            for m in range(N):
                cnt1 = 1
                cnt2 = 1
                for n in range(1,N):
                    if arr[m][n] == arr[m][n-1]:
                        cnt1 += 1
                    else:
                        if result < cnt1:
                            result =cnt1
                        cnt1 = 1
                    if arr[n][m] == arr[n-1][m]:
                        cnt2 += 1
                    else:
                        if result < cnt2:
                            result = cnt2
                        cnt2 = 1
                if result < cnt1:
                    result = cnt1
                if result < cnt2:
                    result = cnt2
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

print(result)