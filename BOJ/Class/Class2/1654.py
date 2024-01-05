# 랜선 자르기 / 실버2

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

l, r = 1, max(lst)
while l <= r:
    cnt = 0
    m = (l + r) // 2
    for x in lst:
        cnt += x // m
    if cnt >= N:
        l = m+1
    else:
        r = m-1
print(m if cnt >= N else m-1)