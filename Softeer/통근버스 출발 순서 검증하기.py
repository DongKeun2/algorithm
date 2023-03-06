# [인증평가(4차) 기출] 통근버스 출발 순서 검증하기 Lv3
# 249ms 38.41Mb

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(N):
    lst = []
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            lst.append(j)
        elif arr[i] > arr[j]:
            result += len(lst)

print(result)