# 이분 그래프

from collections import deque
import sys
input = sys.stdin.readline

# bfs
def sol(s):
    global result

    q = deque()
    q.append(s)
    n = vst[s]
    while q:
        s = q.popleft()
        n = vst[s]
        for x in arr[s]:
            # 아직 방문하지 않은 곳이라면 출발지보다 1 큰 수 저장
            if vst[x] == -1:
                vst[x] = n+1
                q.append(x)
            else:
                # 짝수와 짝수가 만나거나, 홀수와 홀수가 만난다면 이분그래프 성립x
                if (vst[x]%2==0 and vst[s]%2==0) or (vst[x]%2==1 and vst[s]%2==1):
                    result = 'NO'
                    return 


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    # 인접 리스트 생성
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # 결과값 YES로 지정, 예외 발생 시 NO로 바꾸어 줌
    # (예외 : 이분그래프를 만족하지 않을 때)
    result = 'YES'
    vst = [-1] * (V+1)
    for i in range(1, V+1):
        if result == 'NO':
            break
        if vst[i] == -1:
            vst[i] = 0
            sol(i)

    print(result)
