# 모든 순열
# 브루트 포스, 백트래킹

def sol():
    if len(result) == N:
        print(*result)
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                result.append(lst[i])
                sol()
                result.pop()
                v[i] = 0
        return

N = int(input())
lst = [i for i in range(1, N+1)]
result = []
v = [0 for _ in range(N)]
sol()