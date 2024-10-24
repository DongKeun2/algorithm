# 구간 곱 구하기 / 골드1

import sys
input = sys.stdin.readline
MOD = 1000000007

N, M, K = map(int, input().split())

arr = [0] * (N)
for i in range(N): arr[i] = int(input())

tree = [0] * (4*N)
def init(n, l, r):
    if l == r: tree[n] = arr[l]
    else:
        m = (l+r)//2
        tree[n] = init(n*2, l, m) * init(n*2+1, m+1, r)
    return tree[n] % MOD
init(1, 0, N-1)


def update(n, l, r, t, v):
    if t < l or r < t: return
    if l == r: 
        tree[n] = v
        return
    m = (l+r)//2
    update(n*2, l, m, t, v)
    update(n*2+1, m+1, r, t, v)
    tree[n] = tree[n*2] * tree[n*2+1] % MOD


def get_answer(n, l, r, s, e):
    if e < l or r < s: return 1
    if s <= l and r <= e: return tree[n]
    m = (l+r)//2
    return (get_answer(n*2, l, m, s, e) * get_answer(n*2+1, m+1, r, s, e)) % MOD


for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
        arr[b-1] = c
    else: print(get_answer(1, 0, N-1, b-1, c-1)) 