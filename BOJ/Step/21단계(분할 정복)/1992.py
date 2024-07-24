# 쿼드트리

def sol(tmp):
    n = len(tmp)

    s = 0
    for i in range(n):
        for j in range(n):
            s += int(tmp[i][j])

    if s == 0:
        return '0'
    if s == n**2:
        return '1'

    return '(' + ''.join((
        sol([lst[:n//2] for lst in tmp[:n//2]]),
        sol([lst[n//2:] for lst in tmp[:n//2]]),
        sol([lst[:n//2] for lst in tmp[n//2:]]),
        sol([lst[n//2:] for lst in tmp[n//2:]]),
    )) + ')'

N = int(input())

arr = [list(input()) for _ in range(N)]

result = sol(arr)

print(''.join(s for s in result))