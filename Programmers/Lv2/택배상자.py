# 연습문제 LV2

# st활용 문제설명 그대로 구현
def solution(order):
    n = len(order)
    idx = 0
    st = []
    answer = 0
    for i in range(1, n+1):
        if order[idx] == i:
            answer += 1
            idx += 1
        else:
            st.append(i)
        while st:
            if st[-1] == order[idx]:
                st.pop()
                answer += 1
                idx += 1
            else:
                break
    return answer