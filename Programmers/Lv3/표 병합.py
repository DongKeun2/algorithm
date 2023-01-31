# 2023 카카오 블라인드
# Lv3

def solution(commands):
    arr = [[''] * 51 for _ in range(51)]
    tmp = [[[] for _ in range(51)] for _ in range(51)]
    
    answer = []
    for command in commands:
        lst = command.split(' ')
        t = lst[0]
        if t == 'UPDATE':
            # r, c 위치 값을 v로 변경
            # 병합된 셀이라면 병합된 모든 곳 v로 변경
            if len(lst) == 4:
                r, c, v = lst[1:]
                r, c = int(r), int(c)
                arr[r][c] = v
                if tmp[r][c]:
                    mr, mc = tmp[r][c]
                    for i in range(51):
                        for j in range(51):
                            if tmp[i][j] == [mr, mc]:
                                arr[i][j] = v
            
            # v1을 v2로 변경
            else:
                v1, v2 = lst[1:]
                for i in range(51):
                    for j in range(51):
                        if arr[i][j] == v1:
                            arr[i][j] = v2
        elif t == 'MERGE':
            r1, c1, r2, c2 = lst[1:]
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            
            # 값 설정
            if arr[r1][c1]:
                value = arr[r1][c1]
            elif arr[r2][c2]:
                value = arr[r2][c2]
            else:
                value = ''
            
            # 셀 병합 기준 설정
            if tmp[r1][c1]:
                mr1, mc1 = tmp[r1][c1]
            else:
                mr1, mc1 = r1, c1
            if tmp[r2][c2]:
                mr2, mc2 = tmp[r2][c2]
            else:
                mr2, mc2 = r2, c2
            
            # 병합된 모든 곳 값 변경
            for i in range(51):
                for j in range(51):
                    if (i == r1 and j == c1) or (i == r2 and j == c2):
                        tmp[i][j] = [mr1, mc1]
                        arr[i][j] = value

                    elif tmp[i][j] == [mr1, mc1] or tmp[i][j] == [mr2, mc2]:
                        tmp[i][j] = [mr1, mc1]
                        arr[i][j] = value
                        
        elif t == 'UNMERGE':
            r, c = lst[1:]
            r, c = int(r), int(c)
            if arr[r][c]:
                value = arr[r][c]
            else:
                value =''
            
            # 병합 해제
            if tmp[r][c]:
                mr, mc = tmp[r][c]

                for i in range(51):
                    for j in range(51):
                        if tmp[i][j] == [mr, mc]:
                            arr[i][j] = ''
                            tmp[i][j] = []
            arr[r][c] = value
            
        else:
            r, c = lst[1:]
            r, c = int(r), int(c)
            if arr[r][c]:
                answer.append(arr[r][c])
            else:
                answer.append('EMPTY')
    return answer