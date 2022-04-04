# 트리의 부모 찾기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# 각 노드의 인접리스트 생성
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 1번부터 시작하여 vst에 부모노드 기록
q = deque()
q.append(1)
vst = [0] * (N+1)
while q:
    s = q.popleft()
    for e in arr[s]:
        if vst[e] == 0:
            vst[e] = s
            q.append(e)

result = vst[2:]
for ans in result:
    print(ans)
