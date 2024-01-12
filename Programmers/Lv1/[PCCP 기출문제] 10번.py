# [PCCE 기출문제] 10번 / 데이터 분석

# 정렬
enum = {
    'code': 0,
    'date': 1,
    'maximum': 2,
    'remain': 3
}

def solution(data, ext, val_ext, sort_by):
    answer = []
    for lst in data:
        if lst[enum[ext]] < val_ext:
            answer.append(lst)
    answer.sort(key=lambda lst:lst[enum[sort_by]])
    return answer