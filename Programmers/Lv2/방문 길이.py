# Summer/Winter Coding(~2018) Lv2

dct = {
    'U': (1, 0),
    'D': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

# 4차원 배열 생성, 양쪽으로 확인
def solution(dirs):
    vst = [[[[0]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    si, sj = 5, 5
    answer = 0
    # -5,-5를  0,0에 대입하여 5,5를 시작좌표로 설정
    # 0~10 인덱스 내에서 이동
    for d in dirs:
        ei = si + dct[d][0]
        ej = sj + dct[d][1]
        # 이동할 수 있으면 이동하며 처음가는 길이라면 +1
        if 0 <= ei <= 10 and 0 <= ej <= 10:
            if vst[si][sj][ei][ej] == 0 and vst[ei][ej][si][sj] == 0:
                vst[si][sj][ei][ej] = 1
                vst[ei][ej][si][sj] = 1
                answer += 1
            si, sj = ei, ej
    
    return answer