# [SW 문제해결 기본] 10일차 - Contact

def sol(q):
    global result
    qq = []
    flag = 0
    while q:
        n = q.pop()
        for m in arr[n]:
            if vst[m] == 0:
                qq.append(m)
                vst[m] = 1
                flag = 1
    if flag == 1:
        result = max(qq)
        sol(qq)
    return

T = 10
for test_case in range(1, T+1):
    N, root = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = [[] for _ in range(101)]
    for i in range(N//2):
        arr[lst[i*2]].append(lst[i*2+1])

    vst = [0]*101
    vst[root] = 1
    result = root
    q = [root]
    sol(q)

    print(f'#{test_case} {result}')
    