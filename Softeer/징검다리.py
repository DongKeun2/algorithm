# 징검다리 Lv3

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열 구하기
tmp = [0] * N
tmp[0] = 1
for i in range(N):
    max_cnt = 0
    for j in range(i):
        if lst[i] > lst[j] and max_cnt < tmp[j]:
            max_cnt = tmp[j]
    tmp[i] = max_cnt + 1

print(max(tmp))