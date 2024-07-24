# 나머지 합
# 148532KB, 680ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

tmp = [0] * (M)
tmp[0] = 1

# Sm - Sn이 M의 배수라면 1개의 경우가 생기므로
# 이전에 같은 나머지를 갖는 S의 수가 중요하다.
S = 0
result = 0
for n in lst:
    S += n
    result += tmp[S%M]
    tmp[S%M] += 1

print(result)
