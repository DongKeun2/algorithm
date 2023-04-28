# 요격 시스템 Lv2
# 연습문제

# 종료 지점이 큰 것부터 확인
# 해당 지점보다 시작 지점이 큰 곳은 함께 요격 가능하므로 now를 갱신
# 만약 종료 지점이 요격 지점보다 이르다면 함꼐 요격이 불가능하므로 answer ++
def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1], reverse=True)

    now = 10**16
    for s, e in targets:
        if now < s:
            now = s
        elif now >= e:
            now = s
            answer += 1
        
    return answer