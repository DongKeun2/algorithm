# 오름차순 1차원 배열로 변환
# 가장 낮은곳부터 비용을 구해가며 최솟값으로 갱신
def solution(land, P, Q):
    arr = []
    for lst in land:
        arr += lst
    arr.sort()
    
    # 최초 비용 계산(가장 낮은 층)
    n = len(arr)
    min_h, max_h = arr[0], arr[-1]
    cost = 0
    for i in range(n):
        cost += (arr[i] - min_h) * Q
    answer = cost
    
    # 층이 높아지면 해당 층에 대해 계산
    now_h = min_h
    for i in range(n):
        if now_h < arr[i]:
            cost += (arr[i] - now_h) * i * P
            cost -= (arr[i] - now_h) * (n-i) * Q
            now_h = arr[i]
            answer = min(answer, cost)
    
    return answer