# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

def sol(lst, s):
    global result
    code = []
    flag = 0
    while s <= M:
        if len(code) >= 8:
            break
        if flag == 1:
            break
        v = ''.join(str(x) for x in lst[s:s+7])
        for n in range(10):
            if  v == key[n]:
                s += 7
                code.append(n)
                break
        else:
            flag = 1

    if len(code) == 8:
        tot = 0
        for j in range(8):
            if j % 2:
                tot += code[j]
            else:
                tot += code[j] * 3

        if tot % 10 == 0:
            result = sum(code)
    return


T = int(input())

key = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011'
]

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input())) for _ in range(N)]

    result = 0
    for i in range(N):
        if result != 0:
            break

        if arr[i].count(0) == M:
            continue
        else:
            for j in range(M-7):
                if result != 0:
                    break
                sol(arr[i], j)

    print(f'#{test_case} {result}')
