# 택배 배달과 수거하기 Lv2
# 2023 KAKAO BLIND RECRUITMENT

# 가장 먼 집부터 탐색
def solution(cap, n, deliveries, pickups):  
    answer = 0
    d, p = cap, cap
    for i in range(n)[::-1]:
        if not answer and (deliveries[i] or pickups[i]):
            answer += (i+1)*2
        d -= deliveries[i]
        p -= pickups[i]
        # 현재 가진 것으로 배달 및 수거가 불가능한 경우, 한 번 왕복
        while d < 0 or p < 0:
            d += cap
            p += cap
            answer += (i+1)*2
            
    return answer