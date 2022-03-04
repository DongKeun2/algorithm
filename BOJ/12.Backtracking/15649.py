# N과 M(1)

def sol(lst):
    if len(result) == M:
        print(*result)
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                result.append(lst[i])
                sol(lst)
                result.pop()
                v[i] = 0
        return

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
result = []
v = [0 for _ in range(N)]
sol(lst)