# 테트로미노

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 결과값 초기화
result = 0

# ㅡㅡㅡㅡ 모양
## (가로)
for i in range(N):
    for j in range(M-3):
        if result < sum(arr[i][j:j+4]):
            result = sum(arr[i][j:j+4])
## (세로)
for i in range(M):
    for j in range(N-3):
        s = 0
        for k in range(j, j+4):
            s += arr[k][i]
        if result < s:
            result = s


# ㅡㅡㅡ 모양
## (가로)
for i in range(N):
    for j in range(M-2):
        # 위 쪽에서 최댓값 하나
        s = sum(arr[i][j:j+3])
        if i+1 < N:
            s += max(arr[i+1][j:j+3])
        if result < s:
            result = s

        # 아랫쪽에서 최댓값 하나
        s = sum(arr[i][j:j+3])
        if i-1 >= 0:
            s += max(arr[i-1][j:j+3])
        if result < s:
            result = s
## (세로)
for j in range(M):
    for i in range(N-2):
        s = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        if j-1 >= 0:
            s += max(arr[i][j-1], arr[i+1][j-1], arr[i+2][j-1])
        if result < s:
            result = s
        
        s = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        if j+1 < M:
            s += max(arr[i][j+1], arr[i+1][j+1], arr[i+2][j+1])
        if result < s:
            result = s

# ㅡㅡ 모양
## (가로)
for i in range(N):
    for j in range(M-1):
        s = sum(arr[i][j:j+2])
        if i-1 >= 0:
            if j-1 >= 0 and j+2 < M:
                s+= max(arr[i-1][j-1]+arr[i-1][j], arr[i-1][j]+arr[i-1][j+1], arr[i-1][j+1]+arr[i-1][j+2])
            elif j-1 >= 0:
                s+= max(arr[i-1][j-1]+arr[i-1][j], arr[i-1][j]+arr[i-1][j+1])
            elif j+2 < M:
                s += max(arr[i-1][j]+arr[i-1][j+1], arr[i-1][j+1]+arr[i-1][j+2])
            else:
                s += arr[i-1][j]+arr[i-1][j+1]
        if result < s:
            result = s

        s = sum(arr[i][j:j+2])
        if i+1 < N:
            if j-1 >= 0 and j+2 < M:
                s+= max(arr[i+1][j-1]+arr[i+1][j], arr[i+1][j]+arr[i+1][j+1], arr[i+1][j+1]+arr[i+1][j+2])
            elif j-1 >= 0:
                s+= max(arr[i+1][j-1]+arr[i+1][j], arr[i+1][j]+arr[i+1][j+1])
            elif j+2 < M:
                s += max(arr[i+1][j]+arr[i+1][j+1], arr[i+1][j+1]+arr[i+1][j+2])
            else:
                s += arr[i+1][j]+arr[i+1][j+1]
        if result < s:
            result = s
## (세로)
for i in range(M):
    for j in range(N-1):
        s = arr[j][i] + arr[j+1][i]
        if i-1 >= 0:
            if j-1 >= 0 and j+2 < N:
                s+= max(arr[j-1][i-1]+arr[j][i-1], arr[j][i-1]+arr[j+1][i-1], arr[j+1][i-1]+arr[j+2][i-1])
            elif j-1 >= 0:
                s+= max(arr[j-1][i-1]+arr[j][i-1], arr[j][i-1]+arr[j+1][i-1])
            elif j+2 < N:
                s += max(arr[j][i-1]+arr[j+1][i-1], arr[j+1][i-1]+arr[j+2][i-1])
            else:
                s += arr[j][i-1]+arr[j+1][i-1]
        if result < s:
            result = s

        s = arr[j][i] + arr[j+1][i]
        if i+1 < M:
            if j-1 >= 0 and j+2 < N:
                s+= max(arr[j-1][i+1]+arr[j][i+1], arr[j][i+1]+arr[j+1][i+1], arr[j+1][i+1]+arr[j+2][i+1])
            elif j-1 >= 0:
                s+= max(arr[j-1][i+1]+arr[j][i+1], arr[j][i+1]+arr[j+1][i+1])
            elif j+2 < N:
                s += max(arr[j][i+1]+arr[j+1][i+1], arr[j+1][i+1]+arr[j+2][i+1])
            else:
                s += arr[j][i+1]+arr[j+1][i+1]
        if result < s:
            result = s

print(result)
