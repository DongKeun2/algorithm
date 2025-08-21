# 2020 카카오 인턴십 / [카카오 인턴] 보석 쇼핑, Lv2

# 딕셔너리 풀이, 미리 보석의 종류 개수 l 구해놓기
# 모든 보석이 dct에 담기면 answer 확인
def solution(gems):
    l = len(set(gems))
    dct = {}
    n = len(gems)
    answer = [0, n]
    min_v = 0
    for i in range(n):
        if gems[i] in dct and dct[gems[i]] == min_v:
            dct[gems[i]] = i
            min_v = min(dct.values())
        else: dct[gems[i]] = i
        if len(dct.keys()) >= l:
            if i - min_v < answer[1] - answer[0]: answer = [min_v + 1, i + 1]
    return answer


# 효율성 11~15 시간초과
# def solution(gems):
#     s = set(gems)
#     l = len(s)
    
#     dct = {}
#     n = len(gems)
#     answer = [0, n]
#     min_v = n
#     max_v = 0
#     for i in range(n):
#         dct[gems[i]] = i
        
#         if len(dct.keys()) >= l:
#             if answer[1] - answer[0] > max(dct.values()) - min(dct.values()):
#                 answer = [min(dct.values())+1, max(dct.values())+1]
#     return answer