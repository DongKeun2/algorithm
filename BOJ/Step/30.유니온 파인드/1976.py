# 여행 가자

def sol(n):
    q = [n]

    vst = [0] * N
    vst[n] = 1
    while q:
        s = q.pop(0)
        for i in range(N):
            if arr[s][i] == 1 and vst[i] == 0:
                vst[i] = 1
                tmp.append(i)
                q.append(i)


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = list(map(int, input().split()))

tmp = [lst[0] - 1]
sol(lst[0] - 1)

result = "YES"
for i in range(M):
    n = lst[i] - 1
    
    if n not in tmp:
        result = "NO"
        break

print(result)