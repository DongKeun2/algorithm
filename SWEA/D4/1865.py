# 동철이의 일 분배

def sol(idx, tot):
    global result

    if tot <= result:
        return

    if idx >= N:
        if result < tot:
            result = tot
        return

    for i in range(N):
        if vst[i] == 0:
            vst[i] = 1
            sol(idx+1, tot*(arr[idx][i]/100))
            vst[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    vst = [0] * (N)
    result = 0
    sol(0, 1)
    result *= 100

    print(f'#{test_case} {result:.6f}')