# 다리를 지나는 트럭 Lv2
# 스택/큐

# 큐 풀이
# 시간을 1초씩 늘려가며 확인
# 다리를 건너는 트럭의 무게 w와 weight을 비교
# 트럭이 다리를 건널 수 있으면 (나가는 시간, 트럭의 무게)를 큐에 저장
# 나가는 시간이 된 트럭은 큐에서 제거
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    idx = 0
    w = 0
    q = deque([])
    while idx < len(truck_weights):
        time += 1
        while q:
            if q[0][0] <= time:
                w -= q[0][1]
                q.popleft()
            else:
                break
                
        if w + truck_weights[idx] <= weight:
            w += truck_weights[idx]
            q.append((time + bridge_length, truck_weights[idx]))
            idx += 1
                
    answer = q[-1][0]
    return answer