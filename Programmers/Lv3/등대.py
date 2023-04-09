# 등대 Lv3
# 연습문제

# DFS 풀이
# 임의 노드(1)를 루트로 설정
# 리프노드는 등대를 키지 않는다.
# 자식 노드가 모두 꺼져 있다면 등대를 켠다. 
import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    global answer
    def dfs(num):
        global answer
        vst[num] = True
        
        cnt = 0
        if arr[num]:
            for e in arr[num]:
                if vst[e] == False:
                    cnt += dfs(e)
            if cnt:
                answer += 1
                return 0
            else:
                return 1
        else:
            return 1
        
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    for s, e in lighthouse:
        arr[s].append(e)
        arr[e].append(s)
    
    vst = [False] * (n+1)
    dfs(1)
    return answer