# 회의실 배정 / 실버1

import sys
input = sys.stdin.readline

# 1 <= N <= 100000
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: -x[1])

start = arr[0][0]
end = arr[0][1]
result = 1
for s, e in arr:
    if e <= start:
        start = s
        end = e
        result += 1
    else:
        if start <= s:
            start = s
            end = e
print(result)

