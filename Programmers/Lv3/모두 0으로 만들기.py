# 모두 0으로 만들기 Lv3
# 월간 코드 챌린지 시즌2

import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):
    global answer
    # 예외처리
    if sum(a):
        return -1
    
    # DFS 풀이
    # 리프노드부터 확인하여 가중치가 있는 경우 0으로 만들어줌
    # 루트노드까지 진행했을 때 루트노드가 0이라면 가능한 경우
    # 루트노드가 0이 아니라면 불가능한 경우
    def sol(x, rep):
        global answer
        if arr[x]:
            for y in arr[x]:
                if vst[y] == 0:
                    vst[y] = 1
                    sol(y, x)
            if a[x]:
                if x == 0:
                    answer = -1
                    return
                a[rep] += a[x]
                answer += abs(a[x])
                a[x] = 0
        else:
            if a[x]:
                a[rep] += a[x]
                answer += abs(a[x])
                a[x] = 0
    
    
    n = len(a)
    arr = [[] for _ in range(n)]
    for s, e in edges:
        arr[s].append(e)
        arr[e].append(s)
    
    vst = [0] * n
    vst[0] = 1
    answer = 0
    sol(0, 0)
    return answer