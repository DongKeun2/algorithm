# N과 M(8)

def sol(lst):
    if len(result) == M:
        a = [x for x in result]
        arr.append(a)
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

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []
arr = []
sol(lst)

arr.sort()
for i in range(len(arr)):
    print(*arr[i])