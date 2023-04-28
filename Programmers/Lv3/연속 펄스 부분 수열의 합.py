# 연속 펄스 부분 수열의 합 Lv3
# 연습문제

# 1부터 시작하는 lst1, -1부터 시작하는 lst2
# 누적합을 구해서 저장
# 부분 수열의 합 중 가장 큰 값을 확인
## 각 자리를 마지막 자리라 가정, 첫 자리는 v1, v2를 활용
def solution(sequence):
    n = len(sequence)
    lst1 = [0] * n
    lst1[0] = sequence[0]
    lst2 = [0] * n
    lst2[0] = -sequence[0]
    for i in range(1, n):
        lst1[i] = lst1[i-1] + ((-1)**i)*sequence[i]
        lst2[i] = lst2[i-1] + ((-1)**(i+1))*sequence[i]
    
    answer = abs(sequence[0])
    v1 = 0
    v2 = 0
    for i in range(n):
        if v1 > lst1[i]:
            v1 = lst1[i]
        if v2 > lst2[i]:
            v2 = lst2[i]
        answer = max(answer, lst1[i] - v1, lst2[i] - v2)
        
    return answer