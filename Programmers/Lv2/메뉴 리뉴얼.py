# 2021 카카오 블라인드 LV2

from itertools import combinations

def solution(orders, course):
    # 조합 별 개수 구하기
    dct = {}
    for order in orders:
        for n in course:
            if len(order) >= n:
                arr = combinations(order, n)
                for word in arr:
                    s = ''.join(sorted(list(word)))
                    if s in dct:
                        dct[s] += 1
                    else:
                        dct[s] = 1
    
    # 코스 길이 별 최대 개수 구하기
    result = {}
    for key, value in dct.items():
        if value >= 2:
            for n in course:
                if len(key) == n:
                    if n in result:
                        if result[n] < value:
                            result[n] = value
                    else:
                        result[n] = value
    
    # 최대 개수에 맞는 조합만 담아서 정렬
    answer = []
    for key, value in dct.items():
        for n in course:
            if len(key) == n and n in result and value == result[n]:
                    answer.append(key)
    answer.sort()
    return answer