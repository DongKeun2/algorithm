# 교점에 별 만들기 Lv2
# 위클리 챌린지

def solution(line):
    # set A에 교점의 좌표 저장
    def sol(idx):
        if idx >= n-1:
            return
        a,b,e = line[idx]
        for i in range(idx+1, n):
            c, d, f = line[i]
            if a*d != b*c:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x == int(x) and y == int(y):
                    A.add((int(x),int(y)))
        sol(idx+1)
        
        
    n = len(line)
    A = set()
    sol(0)
    min_x = 10**18
    max_x = -10**18
    min_y = 10**18
    max_y = -10**18
    for x,y in A:
        if max_x < x:
            max_x = x
        if min_x > x:
            min_x = x
        if max_y < y:
            max_y = y
        if min_y > y:
            min_y = y
    
    # arr에 0,0시작으로 별 모양 저장
    arr = ['.'*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for x,y in A:
        arr[y-min_y] = arr[y-min_y][:x-min_x] + '*' + arr[y-min_y][x-min_x+1:]

    # arr를 위에서부터 담아서 출력
    answer = []
    for lst in arr[::-1]:
        answer.append(lst)
    return answer