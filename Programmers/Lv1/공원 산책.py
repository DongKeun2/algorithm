# 공원 산책 Lv1
# 연습문제


# for else활용 조건에 맞을 때만 이동 
dct = {
    'N' : (-1, 0),
    'S' : (1, 0),
    'W' : (0, -1),
    'E' : (0, 1)
}
def solution(park, routes):
    n = len(park)
    m = len(park[0])
    si, sj = -1, -1
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                si = i
                sj = j
    
    for route in routes:
        op, r = route.split()
        r = int(r)
        d = dct[op]
        ni, nj = si, sj
        for _ in range(1, r+1):
            ni += d[0]
            nj += d[1]
            if 0 <= ni < n and 0 <= nj < m:
                if park[ni][nj] == 'X':
                    break
            else:
                break
        else:
            si, sj = ni, nj
    
    answer = [si, sj]
    return answer