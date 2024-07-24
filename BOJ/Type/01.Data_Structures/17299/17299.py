# 오등큰수

import sys
input = sys.stdin.readline
from collections import Counter as cnt

N = int(input())

n = list(map(int, input().split()))

cntn = cnt(n)
st = [0]
result = [-1] * N
for i in range(1, N):
    while st and cntn.get(n[st[-1]]) < cntn.get(n[i]):
        result[st.pop()] = (n[i])
    st += [i]

print(*result)