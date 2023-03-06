# [인증평가(4차) 기출] 슈퍼컴퓨터 클러스터 Lv3
# 145ms 51.45Mb

import sys
input = sys.stdin.readline

# 이분 탐색
N, B = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
l = lst[0]
r = lst[-1] + 10**9
while l < r:
    m = (l+r) // 2
    cnt = 0
    for i in range(N):
        if cnt > B:
            break
        if lst[i] < m:
            cnt += (m-lst[i]) ** 2
    if cnt > B:
        r = m
    else:
        l = m+1

result = l-1
print(result)