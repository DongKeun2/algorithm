# [S/W 문제해결 응용] 10일차 - 작업 순서

T = 10

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = [[0] for _ in range(V+1)]

    for i in range(1, E*2+1, 2):
        arr[lst[i]].append(lst[i-1])

    cnt = 0
    result = []
    while cnt < V:
        for i in range(1, V+1):
            if arr[i] != [] and arr[i][-1] == 0:
                result.append(i)
                arr[i] = []
                cnt += 1
                for j in range(1, V+1):
                    if i in arr[j]:
                        arr[j].remove(i)

    print(f'#{test_case}', *result)