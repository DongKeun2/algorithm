# DFS 스페셜 저지

import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
arr[0].append(1)

lst = list(map(int, input().split()))

idx = 1
st = [1]
result = 1
while True:
    if st == []:
        result = 0
        break
    if idx >= N:
        break

    if lst[idx] in arr[st[-1]]:
        st.append(lst[idx])
        idx += 1
    else:
        st.pop()

print(result)
