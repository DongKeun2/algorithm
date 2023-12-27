# [PCCP 기출문제] 1번 / 붕대 감기

# bandage: [ 시전시간, 초당 회복량, 추가 회복량]
# 1 <= health <= 1000 // 최대 체력
# attacks[i]: [공격 시간, 피해량]
# 1 <= attacks.length <= 100
def solution(bandage, health, attacks):
    # 1 브루트 포스
    time = 0
    now = health
    cnt = 0
    end_time = attacks[-1][0]
    idx = 0
    while time <= end_time and idx < len(attacks):
        if time == attacks[idx][0]:
            now -= attacks[idx][1]
            if now <= 0:
                return -1
            cnt = 0
            idx += 1
        else:
            cnt += 1
            now += bandage[1]
            if cnt >= bandage[0]:
                now += bandage[2]
        if now >= health:
            now = health
        time += 1
    
    answer = now
    return answer