# 커피숍2 / 골드1

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0] * (4*N)
def init(n, l, r):
    if l == r: tree[n] = arr[l]
    else:
        m = (l+r)//2
        tree[n] = init(n*2, l, m) + init(n*2+1, m+1, r)
    return tree[n]
init(1, 0, N-1)


def update(n, l, r, t, d):
    if t < l or r < t: return
    tree[n] += d
    if l == r: return
    m = (l+r)//2
    update(n*2, l, m, t, d)
    update(n*2+1, m+1, r, t, d)


def answer(n, l, r, s, e):
    if e < l or r < s: return 0
    if s <= l and r <= e: return tree[n]
    m = (l+r)//2
    return answer(n*2, l, m, s, e) + answer(n*2+1, m+1, r, s, e)


for _ in range(Q):
    x, y, a, b = map(int, input().split())
    print(answer(1, 0, N-1, min(x-1, y-1), max(x-1, y-1)))
    update(1, 0, N-1, a-1, b-arr[a-1])
    arr[a-1] = b