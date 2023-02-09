# 2021 dev-matching 웹 백엔드 개발자(상반기) Lv3

def solution(enroll, referral, seller, amount):
    # 10%가 1 미만이면 해당 조직원만 이익금을 가져감
    # 1 이상이면 10%를 상위 조직원에게 넘겨줌
    # 1미만이 되거나 민호가 가져가는 경우까지 반복
    def sol(idx, cnt):
        if idx == -1:
            return
        p = cnt
        up = int(p / 10)
        if up:
            p -= up
            answer[idx] += p
            sol(rep[idx], up)
        else:
            answer[idx] += p
    
    # 초기 설정
    # dct = {name : i}
    # tmp = {i : name}
    # rep = [] 상위 조직원 i저장
    # 상위 조직원이 없으면 rep에 -1 저장
    n = len(enroll)
    m = len(seller)
    dct = {}
    tmp = {}
    rep = [-1] * n
    for i in range(n):
        dct[enroll[i]] = i
        tmp[i] = enroll[i]
    dct['-'] = -1
    for i in range(n):
        rep[i] = dct[referral[i]]
        
    # 판매원,이익금 재귀
    answer = [0] * n
    for i in range(m):
        sol(dct[seller[i]], amount[i]*100)
        
    return answer