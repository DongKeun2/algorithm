# 2022 카카오 블라인드 Lv2

import math

def solution(fees, records):
    # 차량번호별 입출차 내역 기록
    dct = {}
    for record in records:
        time, number, x = record.split(' ')
        h, m = time.split(':')
        t = int(h)*60 + int(m)
        if number in dct:
            dct[number].append(t)
        else:
            dct[number] = [t]
    
    # 차량 번호순서대로 lst에 정렬
    lst = []
    for key in dct.keys():
        lst.append(int(key))
    lst.sort()
    
    # lst에서 차량번호 순서대로 dct에서 꺼내어 계산
    answer = []
    for car in lst:
        number = '0' * (4-len(str(car))) + str(car)
        time = 0
        for i in range(0, len(dct[number]), 2):
            if i+1 < len(dct[number]):
                time += dct[number][i+1] - dct[number][i]
            else:
                 time += (23*60 + 59) - dct[number][i]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3])
        
    return answer