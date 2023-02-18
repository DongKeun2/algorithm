# [21년 재직자 대회 예선] 비밀 메뉴 Lv2

import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
lst = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr += arr
answer = 'normal'
for i in range(2*N):
    if arr[i:i+M] == lst:
        answer = 'secret'
        break

print(answer)