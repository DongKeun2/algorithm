# 알파벳
# 그래프이론, 그래프탐색, 깊이우선탐색, 백트래킹
# pypy통과

def sol(si, sj, cnt):
    global result

    for d in range(4):
        ni = si + di[d]
        nj = sj + dj[d]
        if 0<=ni<R and 0<=nj<C and vst[ni][nj] == 0:
            tmp.add(arr[ni][nj])
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