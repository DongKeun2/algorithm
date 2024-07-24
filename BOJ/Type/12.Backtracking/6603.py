# 로또
# 수학, 조합론, 백트래킹, 재귀


while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    N = lst[0]
    lst = lst[1::]
    arr = []
    for i in range(1<<N):
        result = []
        cnt = 0
        for j in range(N):
            if i & (1<<j):
                cnt += 1
                result.append(lst[j])
        if cnt == 6:
            arr.append(result)
    arr.sort()
    for i in range(len(arr)):
        print(*arr[i])
    print()