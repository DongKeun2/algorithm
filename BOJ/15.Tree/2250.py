# 트리의 높이와 너비
# pypy 통과
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 중위 순회, arr에 높이를 인덱스 x좌표 추가
def sol(s, h):
    global x

    if s != -1:
        sol(ch1[s], h+1)
        arr[h].append(x)
        x += 1
        sol(ch2[s], h+1)

N = int(input())

arr = [[] for _ in range(N+1)]
ch1 = [0 for _ in range(N+1)]
ch2 = [0 for _ in range(N+1)]
p = [0 for _ in range(N+1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    ch1[a] = b
    ch2[a] = c
    p[b] = p[c] = a

# 루트 정점 s 찾기
# s의 높이를 1로 나머지 좌표 찾기
x = 1
for i in range(1, N+1):
    if p[i] == 0:
        sol(i, 1)

# 최대 너비 result2 그 때의 높이 result1
result1 = 0
result2 = 0

# 각 높이마다 너비찾기
for i in range(1, len(arr)):
    if arr[i]:
        arr[i].sort
        if result2 < arr[i][-1] - arr[i][0] + 1:
            result2 = arr[i][-1] - arr[i][0] + 1
            result1 = i

print(result1, result2)