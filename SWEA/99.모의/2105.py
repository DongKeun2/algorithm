# 디저트 카페

def sol(si, sj, d, s):
    global cnt
 
    n = vst[si][sj]
    ni = si + di[d]
    nj = sj + dj[d]
    if ni < s:
        return
    elif 0<=ni<N and 0<=nj<N and vst[ni][nj] == 0 and (arr[ni][nj] not in result):
        vst[ni][nj] = n+1
        result.append(arr[ni][nj])
        sol(ni, nj, d, s)
        if d < 3:
            sol(ni, nj, d+1, s)
        vst[ni][nj] = 0
        result.pop()
     
    elif 0<=ni<N and 0<=nj<N and n != 2 and vst[ni][nj] == 1:
        cnt = max(cnt, len(result))
    return
 
 
T = int(input())
 
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
 
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    cnt = -1
    vst = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-2):
        for j in range(1, N-1):
            vst[i][j] = 1
            result = [arr[i][j]]
            sol(i, j, 0 ,i)
            vst[i][j] = 0
 
    print(f'#{test_case} {cnt}')