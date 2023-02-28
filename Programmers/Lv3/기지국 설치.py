# 기지국 설치 Lv3
# Summer/Winter Coding(~2018)

def solution(n, stations, w):
    lst = []
    for station in stations:
        lst.append(station - w)
        lst.append(station+w)
    lst = [0] + lst + [n+1]
    
    # 전파가 안 닿는 구간마다 아파트 개수를 계산
    # 해당 구간에 최소 개수의 기지국을 설치
    step = w*2+1
    answer = 0
    for i in range(0, len(lst), 2):
        if lst[i] < lst[i+1]:
            if (lst[i+1] - lst[i] - 1) % step:
                answer += (lst[i+1] - lst[i] - 1) // step + 1
            else:
                answer += (lst[i+1] - lst[i] - 1) // step
    return answer