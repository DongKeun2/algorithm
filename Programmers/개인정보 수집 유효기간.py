# 2023 카카오 블라인트
# LV1

def solution(today, terms, privacies):
    y0, m0, d0 = map(int, today.split('.'))
    
    dct = {}
    for item in terms:
        key, value = item.split(' ')
        dct[key] = int(value)
    
    answer = []
    for i in range(len(privacies)):
        privacy = privacies[i]
        day, t = privacy.split(' ')
        y1, m1, d1 = map(int, day.split('.'))
        m1 += dct[t]
        if m1 > 12:
            y1 += m1//12
            m1 %= 12
        if m1 == 0:
            y1 -= 1
            m1 = 12
        
        if y1 < y0:
            answer.append(i+1)
        elif y1 == y0 and m1 < m0:
            answer.append(i+1)
        elif y1 == y0 and m1 == m0 and d1 <= d0:
            answer.append(i+1)
        
    return answer