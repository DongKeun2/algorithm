# N과 M(4)

def sol(lst):
    if len(result) == M:
        print(*result)
        return
    else:
        for i in range(N):
            if result:
                if result[-1] <= lst[i]:
                    result.append(lst[i])
                    sol(lst)
                    result.pop()
            else:
                result.append(lst[i])
                sol(lst)
                result.pop()
        return

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
result = []
sol(lst)