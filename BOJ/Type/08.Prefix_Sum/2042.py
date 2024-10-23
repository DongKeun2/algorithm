# 구간 합 구하기 / 골드1

import sys
input = sys.stdin.readline

# 기본 조건 구성
N, M, K = map(int, input().split())
arr = [0] * N
for i in range(N): arr[i] = int(input())

# 세그먼트 트리 구성
tree = [0] * (2*N)
def init(n, l, r):
    if l == r: tree[n] = arr[l]
    else: tree[n] = init(n*2, l, (l+r)//2) + init(n*2 + 1, (l+r)//2 + 1, r)
    return tree[n]
init(1, 0, N-1)

# 트리 업데이트
def update(n, l, r, t, d):
    if l > t or r < t: return
    tree[n] += d
    if l == r: return
    update(n*2, l, (l+r)//2, t, d)
    update(n*2 + 1, (l+r)//2 + 1, r, t, d)

# 구간 합 구하기
def get_sum(n, l, r, s, e):
    if e < l or r < s: return 0
    if s <= l and r <= e: return tree[n]
    return get_sum(n*2, l, (l+r)//2, s, e) + get_sum(n*2 + 1, (l+r)//2 + 1, r, s, e)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, N-1, b-1, diff)
    else: print(get_sum(1, 0, N-1, b-1, c-1))
