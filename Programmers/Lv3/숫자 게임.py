# 숫자 게임 Lv3
# Summer/Winter Coding(~2018)

def solution(A, B):
    A.sort()
    B.sort()
    n = len(A)
    m = len(B)
    
    a = 0
    b = 0
    answer = 0
    # A[a]보다 큰 B의 원소 중 가장 작은 값을 찾는다.
    # 찾으면 결과에 +1 해준 뒤 다음 A[a]에 대해 반복
    while a < n and b < m:
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
        
    return answer