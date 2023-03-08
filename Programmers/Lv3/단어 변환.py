# 단어 변환 Lv3
# 깊이/너비 우선 탐색(DFS/BFS)

def solution(begin, target, words):
    global answer
    # DFS 탐색, tmp에 이미 바꾼 문자 기록
    def sol(S, cnt, tmp):
        global answer
        if answer <= cnt:   # 이미 타겟을 만든 경우 더 많은 변환 불필요
            return
        
        if S == target:     # 갱신
            answer = min(answer, cnt)
            return
        
        # 현재 단어와 words의 단어 비교, 하나의 문자가 다른 경우 재귀
        for W in words:
            if W not in tmp:
                c = 0
                for i in range(n):
                    if S[i] != W[i]:
                        c += 1
                if c == 1:
                    sol(W, cnt+1, tmp + [W])
    answer = 10**18
    n = len(begin)
    sol(begin, 0, [])
    if answer == 10**18:
        answer = 0
    return answer