# 벌꿀 채취

# 채취할 수 있는 벌통 골라내기
def comb(lst):
    rlst = []
    for i in range(1<<len(lst))[::-1]:
        tmp = []
        for j in range(len(lst)):
            if i & (1<<j):
                tmp.append(lst[j])
        if tmp and sum(tmp) <= C:
            if rlst:
                rx = sum(x**2 for x in rlst)
                tx = sum(x**2 for x in tmp)
                if rx < tx:
                    rlst = tmp
            else:
                rlst = tmp
    return rlst


# 두 일꾼이 채취한 벌꿀의 수익 갱신
def check(tot1, tot2):
    global result

    if result < tot1+tot2:
        result = tot1+tot2


# 두번째 일꾼 벌꿀 채취
def sol(si, sj, tot1):
    for j in range(sj+M, N-M+1):
        if C < sum(arr[si][j:j+M]):
            tmp = comb(arr[si][j:j+M])
            tot2 = sum(x**2 for x in tmp)
            check(tot1, tot2)
        else:
            tot2 = sum(x**2 for x in arr[si][j:j+M])
            check(tot1, tot2)

    for i in range(si+1, N):
        for j in range(N-M+1):
            if C < sum(arr[i][j:j + M]):
                tmp = comb(arr[i][j:j + M])
                tot2 = sum(x ** 2 for x in tmp)
                check(tot1, tot2)
            else:
                tot2 = sum(x ** 2 for x in arr[i][j:j + M])
                check(tot1, tot2)


T = int(input())

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 첫번째 일꾼 벌꿀 채취 => sol함수로 두번째 일꾼에게 넘김
    result = 0
    for i in range(N-1):
        for j in range(N-M+1):
            if C < sum(arr[i][j:j + M]):
                tmp = comb(arr[i][j:j + M])
                tot1 = sum(x ** 2 for x in tmp)
                sol(i, j, tot1)
            else:
                tot1 = sum(x ** 2 for x in arr[i][j:j + M])
                sol(i, j, tot1)

    for j in range(N-2*M+1):
        if C < sum(arr[N-1][j:j+M]):
            tmp = comb(arr[N-1][j:j+M])
            tot1 = sum(x**2 for x in tmp)
            sol(N-1, j, tot1)
        else:
            tot1 = sum(x**2 for x in arr[N-1][j:j+M])
            sol(N-1, j, tot1)

    print(f'#{test_case} {result}')