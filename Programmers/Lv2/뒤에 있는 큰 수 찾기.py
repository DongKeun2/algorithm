# 연습문제 Lv2

def solution(numbers):
    # -1로 초기화
    answer = [-1] * (len(numbers)) 
    
    # stack으로 확인
    st = []
    for idx, number in enumerate(numbers):
        # st의 마지막 값이 작은 경우 그 자리에 해당 수를 채움
        while True:
            if st and st[-1][1] < number:
                i, n = st.pop()
                answer[i] = number
            else:
                break
        st.append((idx, number))
        
    return answer