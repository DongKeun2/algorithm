# N과 M(7)

def sol(lst):
    if len(result) == M:
        a = [x for x in result]
        arr.append(a)
        return
    else:
        for i in range(N):
            result.append(lst[i])
            sol(lst)
            result.pop()
        return

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []
arr = []
sol(lst)

arr.sort()
for i in range(len(arr)):
    print(*arr[i])