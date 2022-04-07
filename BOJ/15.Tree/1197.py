# 최소 스패닝 트리

import sys
input = sys.stdin.readline

# 대표정점이 같은지 확인
# 대표 정점까지 가는 길에 들리는 모든 정점에 대표정점 저장
def find_set(n):
    if n == rep[n]:
        return n
    rep[n] = find_set(rep[n])
    return rep[n]


# 두 그룹을 하나로 합쳐주기
def union(u, v):
    rep[find_set(v)] = find_set(u)


V, E = map(int, input().split())

arr = []
for _ in range(E):
    u, v, w = map(int, input().split())
    arr.append((w, u, v))
arr.sort()

rep = [i for i in range(V+1)]
result = 0
cnt = 0
for w, u, v in arr:
    if cnt >= V-1:
        break
    if find_set(u) != find_set(v):
        cnt += 1
        result += w
        union(u, v)

print(result)