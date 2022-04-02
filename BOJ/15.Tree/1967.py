# 트리의 지름

from collections import deque
import sys
# 트리 최대깊이 10000(편향트리)
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 루트에서 가장 먼 노드 s
# s에서 bfs 가장 먼 노드 찾기
def check(s):
    global result
    
    # vst에는 s부터 각 노드까지의 거리 저장
    q = deque()
    q.append(s)
    vst[s] = 0
    while q:
        s = q.popleft()
        n = vst[s]

        # s를 부모로 가지는 노드로 연결 (s의 자식에게 연결)
        for i in range(len(arr)):
            if arr[i] == s and vst[i] == -1:
                vst[i] = n + v[i]
                q.append(i)
    
        # s의 부모에게 연결
        if vst[arr[s]] == -1:
            vst[arr[s]] = vst[s] + v[s]
            q.append(arr[s])
    
    # 저장된 vst 중 최댓값 => 트리의 지름
    result = max(vst)

# 루트에서 가장 먼 노드번호 찾기
def sol(idx, tot):
    global length, midx

    for i in range(len(arr)):
        if arr[i] == idx:
            sol(i, tot+v[i])
            
    if length < tot:
        length = tot
        midx = idx


N = int(input())

arr = [0 for _ in range(N+2)]
v = [0 for _ in range(N+2)]

# arr부모노드 기록, v에 해당 인덱스 노드로 오는 길이 
for _ in range(N-1):
    a, b ,c = map(int, input().split())
    arr[b] = a
    v[b] = c

midx, length = 1, 0
sol(1, 0)

vst = [-1] * (N+2)
result = 0
check(midx)

print(result)