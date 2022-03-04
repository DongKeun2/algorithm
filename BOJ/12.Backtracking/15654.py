# N과 M(5)

def sol(lst):
    if len(result) == M:
        a = [x for x in result]
        arr.append(a)
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
lst = list(map(int, input().split()))
result = []
arr = []
v = [0 for _ in range(N)]
sol(lst)

arr.sort()
for i in range(len(arr)):
    print(*arr[i])