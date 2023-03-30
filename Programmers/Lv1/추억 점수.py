# 추억 점수 Lv1
# 연습문제

# 딕셔너리 활용 이름 : 점수 저장
def solution(name, yearning, photo):
    n = len(name)
    dct = {}
    for i in range(n):
        dct[name[i]] = yearning[i]
        
    answer = []
    for lst in photo:
        cnt = 0
        for a in lst:
            if a in dct:
                cnt += dct[a]
        answer.append(cnt)
    return answer