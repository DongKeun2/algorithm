# 최솟값과 최댓값 / 골드1
# 세그먼트 트리

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * (N)
for i in range(N):
    arr[i] = int(input())


# [최소, 최대]로 세그먼트 트리 생성
tree = [[0, 0] for _ in range(4*N)]
def init(n, l, r):
    if l == r: tree[n][0], tree[n][1] = arr[l], arr[l]
    else:
        m = (l+r)//2
        x, y = init(n*2, l, m), init(n*2 + 1, m+1, r)
        tree[n][0] = min(x[0], y[0])
        tree[n][1] = max(x[1], y[1])
    return tree[n]
init(1, 0, N-1)


# s, e 범위에서 [최솟값, 최댓값]을 구하는 함수
def get_answer(n, l, r, s, e):
    if r < s or e < l: return [10**16, 0]
    if s <= l and r <= e: return [tree[n][0], tree[n][1]]
    if l == r: return [tree[n][0], tree[n][1]]
    m = (l+r)//2
    x, y = get_answer(n*2, l, m, s, e), get_answer(n*2 + 1, m+1, r, s, e)
    return [min(x[0], y[0]), max(x[1], y[1])]


for _ in range(M):
    a, b = map(int, input().split())
    answer = get_answer(1, 0, N-1, min(a, b)-1, max(a, b)-1)
    print(*answer)