# 불량 사용자 Lv3
# 2019 카카오 개발자 겨울 인턴십

def solution(user_id, banned_id):
    global answer
    # dct[s]에 S저장
    # S는 유저 아이디, s는 해당 유저 아이디를 가져올 수 있는 문자열
    def sol(S, s, idx, l):
        if idx > l:
            return
        
        if s in dct:
            dct[s].add(S)
        else:
            dct[s] = set()
            dct[s].add(S)

        sol(S, s, idx+1, l)
        s = s[:idx] + '*' + s[idx+1:]
        sol(S, s, idx+1, l)
    
    
    # 중복되지 않는 제재 아이디를 가져올 수 있는 경우 계산
    def check(idx, n, tmp):
        global answer
        if answer == -1:
            return
        if idx >= n:
            answer.add(tuple(sorted(tmp)))
            return

        if banned_id[idx] in dct:
            lst = dct[banned_id[idx]]
            for x in lst:
                if x not in tmp:
                    check(idx+1, n, tmp+[x])
                    
        else:
            answer = -1
        
    
    # dct에 불량사용자 필터링 별 유저 아이디 저장
    dct = {}
    for S in user_id:
        sol(S, S, 0, len(S))
    
    answer = set()
    n = len(banned_id)
    check(0, n, [])
    
    return len(answer)