# 단속카메라 Lv3
# 탐욕법(Greedy)

# 가장 늦게 진출한 차량부터 순서대로 확인
# 해당 차량에 카메라에 찍히지 않았다면 진입 시각에 카메라 설치
def solution(routes):
    routes.sort(reverse=True)
    lst = []
    for s, e in routes:
        for n in lst:
            if s <= n <= e:
                break
        else:
            lst.append(s)
    
    answer = len(lst)
    return answer