# [1차] 캐시 Lv1
# 2018 KAKAO BLIND RECRUITMENT

# LRU(Least Recently Used)
# k만큼 사이즈를 lst에 저장
# 해당 도시가 존재하면 lst에서 가장 뒤로 보냄
# 존재하지 않으면 0번째를 제외하고 가장 뒤에 해당 도시 추가
def solution(cacheSize, cities):
    answer = 0
    lst = []
    for city in cities:
        city = city.lower()
        
        if city in lst:
            answer += 1
            lst.pop(lst.index(city))
        else:
            answer += 5
            
        lst.append(city)
        if len(lst) > cacheSize:
            lst.pop(0)
            
    return answer