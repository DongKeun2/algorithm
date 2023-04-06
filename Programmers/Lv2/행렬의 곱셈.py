# 행렬의 곱셈 Lv2
# 연습문제

# NxL, LxM 행렬로 가정
# answer은 NxM 행렬
# i, j 위치는 A의 SUM(i행 요소 X B의 j열 요소)
def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    l = len(arr2)
    answer = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            answer[i][j] = 0
            for k in range(l):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer