# 알파벳
# 그래프이론, 그래프탐색, 깊이우선탐색, 백트래킹
# pypy통과

# dfs
# tmp의 길이 cnt (이동거리)
def sol(si, sj, cnt):
    global result

    # 4방향 탐색
    for d in range(4):
        ni = si + di[d]
        nj = sj + dj[d]
        # 방문하지 않았다면 tmp에 추가
        if 0<=ni<R and 0<=nj<C and vst[ni][nj] == 0:
            tmp.add(arr[ni][nj])
            # tmp의 길이가 늘어났다면 중복 x 이동가능
            if len(tmp) == cnt+1:
                vst[ni][nj] = 1
                sol(ni, nj, cnt+1)
                vst[ni][nj] = 0
                tmp.remove(arr[ni][nj])

    if cnt > result:
        result = cnt


R, C = map(int, input().split())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

arr = [list(input()) for _ in range(R)]

result = 1
vst = [[0 for _ in range(C)] for _ in range(R)]
vst[0][0] = 1
tmp = set()
tmp.add(arr[0][0])
sol(0, 0, 1)

print(result)