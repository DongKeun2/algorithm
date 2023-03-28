# 바탕화면 정리 Lv1
# 연습문제

def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    min_x, min_y = m, n
    max_x, max_y = 0, 0
    for y in range(n):
        for x in range(m):
            if wallpaper[y][x] == '#':
                if min_y > y:
                    min_y = y
                if max_y < y+1:
                    max_y = y+1
                    
                if min_x > x:
                    min_x = x
                if max_x < x+1:
                    max_x = x+1
    
    answer = [min_y, min_x, max_y, max_x]
    return answer