# [3차] 파일명 정렬 Lv2
# 2018 KAKAO BLIND RECRUITMENT

# 정렬을 위한 배열 arr 생성
# 파일을 기존 파일명, head, number, 기존 순서로 저장
# head, number, 기존 순서에 따라 정렬
# 정렬된 arr에서 기존 파일명을 출력
def solution(files):
    arr = []
    for idx, value in enumerate(files):
        head = ''
        number = ''
        file = value.lower()
        flag = 0
        for w in file:
            if flag == 1:
                if w.isdigit():
                    number += w
                else:
                    flag = 2
                    break
            elif flag == 0:
                if w.isdigit():
                    flag = 1
                    number += w
                else:
                    head += w
        arr.append([value, head, number, idx])
        
    arr.sort(key = lambda x : (x[1], int(x[2]), x[3]))
    answer = [v[0] for v in arr]
    return answer