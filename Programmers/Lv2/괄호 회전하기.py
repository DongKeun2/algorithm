# 월간 코드 챌린지 시즌2 Lv2

def solution(s):
    # 올바른 괄호 문자열인지 확인
    def sol(W):
        st = []
        for w in W:
            if w == '[' or w == '{' or w == '(':
                st.append(w)
            else:
                if st:
                    x = st.pop()
                    if x == '[':
                        if w != ']':
                            return False
                    elif x == '{':
                        if w != '}':
                            return False
                    else:
                        if w != ')':
                            return False 
                else:
                    return False
        if st:
            return False
        return True
    
    n = len(s)
    
    # s를 n번 회전시키며 매 번 확인
    answer = 0
    for i in range(n):
        s = s[1:] + s[0]
        if sol(s):
            answer += 1
        
    return answer