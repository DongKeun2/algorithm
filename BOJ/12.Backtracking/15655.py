# N과 M(6)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
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
        result.sort()
        arr.append(result)

arr.sort()
for i in range(len(arr)):
    print(*arr[i])