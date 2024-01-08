#  Z / 실버1

def cnt_i(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    idx = 0
    while n >= 2 ** idx:
        idx += 1
    idx -= 1
    return (2 ** idx) ** 2 * 2 + cnt_i(n % 2 ** idx)

def cnt_j(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    idx = 0
    while n >= 2 ** idx:
        idx += 1
    idx -= 1
    return (2 ** idx) ** 2 + cnt_j(n % 2 ** idx)

N, r, c = map(int, input().split())
print(cnt_i(r) + cnt_j(c))