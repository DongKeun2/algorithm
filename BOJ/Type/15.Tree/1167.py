# 트리의 지름

import sys
input = sys.stdin.readline

# 시작 노드에서 가장 먼 곳까지 찾기
def sol(s, tot):
    global result, end

    # 인접리스트에 연결된 곳으로 이동, tot에 거리 누적
    for e, v in arr[s]:
        if vst[e] == 0:
            vst[e] = 1
            sol(e, tot+v)
            vst[e] = 0
    
    # 갱신
    if result < tot:
        result = tot
        end = s


V = int(input())

arr = [[] for _ in range(V+1)]
vst = [0] * (V+1)

for _ in range(V):
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)-1, 2):
        arr[lst[0]].append([lst[i], lst[i+1]])

# 1번 노드에서 가장 먼 노드 end찾기
vst[1] = 1
end, result = 0, 0
sol(1, 0)

# end노드에서 가장 먼 노드까지의 거리 찾기
vst[1] = 0
vst[end] = 1
sol(end, 0)

print(result)
