# 프린터 큐
# 구현 자료구조 시뮬레이션 큐

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    result = []
    arr = []
    for i, v in enumerate(lst):
        arr.append([v,i])

    while arr:
        n = arr.pop(0)
        for m in arr:
            if n[0] < m[0]:
                arr.append(n)
                break
        else:
            result.append(n)
            if n[1] == M:
                break
    
    print(len(result))
    