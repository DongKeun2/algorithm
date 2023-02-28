# 풍선 터트리기 Lv3
# 월간 코드 챌린지 시즌1

# 왼쪽 첫 번쨰 풍선부터 점점 작아지는 수만 확인
# 오른쪽 첫 번째 풍선부터 점점 작아지는 수만 확인
def solution(a):
    def left(idx):
        if idx <= 0:
            return 0
        
        st = []
        for i in range(idx):
            if st:
                if st[-1] > a[i]:
                    st.append(a[i])
            else:
                st.append(a[i])
        return len(st)
        
    def right(idx):
        if idx >= n:
            return 0
        
        st = []
        for i in range(n-1, idx, -1):
            if st:
                if st[-1] > a[i]:
                    st.append(a[i])
            else:
                st.append(a[i])
        return len(st)
    
    # 가장 작은 값 기준으로 왼쪽, 오른쪽 나눠 계산
    n = len(a)
    min_v = 10**10
    min_i = 0
    for i in range(n):
        if a[i] < min_v:
            min_i = i
            min_v = a[i]
            
    answer = left(min_i) + right(min_i) + 1
    return answer