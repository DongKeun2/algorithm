# 올바른 괄호 Lv2
# 스택/큐

# stack활용 풀이
def solution(s):
    st = []
    for w in s:
        if w == '(':
            st.append(w)
        else:
            if st:
                st.pop()
            else:
                return False
    if st:
        return False
    return True