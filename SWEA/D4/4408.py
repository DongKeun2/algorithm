# 자기 방으로 돌아가기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0 for _ in range(200)]

    for i in range(N):
        a, b = arr[i][0], arr[i][1]
        if a > b:
            a, b = b, a

        c = a/2
        d = b/2

        if c == int(c):
            c = int(c) - 1
        else:
            c = int(c)

        if d == int(d):
            d = int(d) - 1
        else:
            d = int(d)

        for j in range(c, d+1):
            cnt[j] += 1

    result = 0
    for c in cnt:
        if result < c:
            result = c

    print(f'#{test_case} {result}')