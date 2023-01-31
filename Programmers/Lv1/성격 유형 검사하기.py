# 2022 카카오 테크 인턴쉽
# lv1

def solution(survey, choices):
    # 설문 결과 반영
    arr = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    n = len(survey)
    for i in range(n):
        if choices[i] < 4:
            arr[survey[i][0]] += 4 - choices[i]
        elif choices != 4:
            arr[survey[i][1]] += choices[i] - 4
    
    # 4가지 지표 확인
    answer = ''
    if arr['R'] < arr['T']:
        answer += 'T'
    else:
        answer += 'R'
    if arr['C'] < arr['F']:
        answer += 'F'
    else:
        answer += 'C'
    if arr['J'] < arr['M']:
        answer += 'M'
    else:
        answer += 'J'
    if arr['A'] < arr['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer