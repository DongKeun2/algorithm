# 완전탐색 Lv2

import sys
sys.setrecursionlimit(10**6)

def solution(word):
    def sol(S, n):
        dct[S] = n
        # 마지막 단어에서 종료
        if S == 'UUUUU':
            return
        
        # 길이가 5가 될때까지 A를 붙여줌
        if len(S) < 5:
            sol(S + 'A', n+1)
            return
        
        # 가장 뒤에 나오는 문자를 다음 문자로 교체
        # U는 다음 문자가 없으므로 제거
        while S[-1] == 'U':
            S = S[:-1]
        x = lst[lst.index(S[-1]) + 1]
        S = S[:-1]
        sol(S + x, n+1)
    
    dct = {}
    lst = ['A', 'E', 'I', 'O', 'U']
    sol('A', 1)
    
    answer = dct[word]
    return answer
