# ABCDE

# dfs
def sol(cnt, n):
    global result

    if cnt >= 5:
        result = 1
        return
    elif result == 1:
        return
    else:
        for x in arr[n]:
            if vst[x] == 0:
                vst[x] = 1
                sol(cnt+1, x)
                vst[x] = 0
    return


N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

vst = [0] * N
result = 0

# 시작위치 선정
for i in range(N):
    vst[i] = 1
    sol(1, i)
    if result == 1:
        break
    vst[i] = 0

print(result)