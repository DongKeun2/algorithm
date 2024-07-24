# 기상캐스터

H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]


result = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    cnt = -1
    flag = 0
    for j in range(W):
        if arr[i][j] == 'c':
            result[i][j] = 0
            cnt = 0
            flag = 1
        else:
            if flag == 1:
                cnt += 1
                result[i][j] = cnt

for i in range(len(result)):
    print(*result[i])