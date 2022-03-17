# 장훈이의 높은 선반

def sol(h, i):
    global result
    if h >= B:
        if result > h-B:
            result = h-B

    elif i >= N:
        pass

    else:
        sol(h, i+1)
        sol(h+H[i], i+1)
    return


T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    result = N*10000
    sol(0, 0)

    print(f'#{test_case} {result}')