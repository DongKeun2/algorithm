# N-Queen

def sol(vst, idx):
    global result

    if idx >= N:
        result += 1
        return

    tmp = [0]*N
    for i in range(len(vst)):
        tmp[vst[i]] = 1
        x = vst[i] - (idx-i)
        y = vst[i] + (idx-i)
        if 0 <= x:
            tmp[x] = 1
        if y < N:
            tmp[y] = 1
    for i in range(N):
        if tmp[i] == 0:
            sol(vst+[i], idx+1)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    result = 0
    sol([], 0)

    print(f'#{test_case} {result}')