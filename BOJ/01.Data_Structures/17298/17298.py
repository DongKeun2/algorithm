# 오큰수
import sys
input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

st = [0]
result = [-1] * N
for i in range(1, N):
    while st and nl[i] > nl[st[-1]]:
        result[st.pop()] = nl[i]
    st += [i]

print(*result)
