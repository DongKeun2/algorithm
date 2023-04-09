# 짝지어 제거하기 Lv2
# 2017 팁스타운

# 스택 풀이
def solution(s):
    st = []
    for w in s:
        if st and w == st[-1]:
            st.pop()
        else:
            st.append(w)
    
    if st:
        return 0

    return 1