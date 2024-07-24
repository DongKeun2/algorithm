# N과 M(2)

N, M = map(int, input().split())
lst = [_ for _ in range(1, N+1)]
arr = []
for i in range(1<<len(lst)):
    cnt = 0
    result = []
    for j in range(len(lst)):
        if i != 0:
            if i & (1<<j):
                cnt += 1
                result.append(lst[j])
                if len(result) > M:
                    break
    if len(result) == M:
        arr.append(result)

arr.sort()
for i in range(len(arr)):
    print(*arr[i])