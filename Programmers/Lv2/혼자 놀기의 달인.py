def solution(cards):
    answer = 0
    
    # 이미 뽑은 카드를 0으로 초기화하며 모든 카드 사용
    # 그룹별 수를 세어 tmp에 저장
    tmp = []
    for i in range(len(cards)):
        s = i
        cnt = 0
        while True:
            if cards[s]:
                n = cards[s]
                cards[s] = 0
            else:
                break
            s = n-1
            cnt += 1
        tmp.append(cnt)
    # 2그룹 이상이면 가장 큰 그룹 두 개의 곱 출력
    if len(tmp) >= 2:
        tmp.sort(reverse=True)
        answer = tmp[0] * tmp[1]
        
    return answer