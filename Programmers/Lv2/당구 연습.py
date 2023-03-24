# 당구 연습 Lv2
# 연습문제

def solution(m, n, startX, startY, balls):
    answer = []

    # 상, 하, 좌, 우의 벽에 부딪히게 한다.
    # 꼭짓점은 고려하지 않아도 된다.
    for x, y in balls:
        a1, a2, a3, a4 = 10**18, 10**18, 10**18, 10**18 
        if startX != x:
            a1 = (2*n - startY - y)**2 + abs(startX-x)**2
            a2 = (startY + y)**2 + abs(startX-x)**2
        elif startY > y:
            a1 = (2*n - startY - y)**2 + abs(startX-x)**2
        else:
            a2 = (startY + y)**2 + abs(startX-x)**2
        
        if startY != y:
            a3 = abs(startY-y)**2 + (startX+x)**2
            a4 = abs(startY-y)**2 + (2*m - startX - x)**2
        elif startX > x:
            a4 = abs(startY-y)**2 + (2*m - startX - x)**2
        else:
            a3 = abs(startY-y)**2 + (startX+x)**2
        answer.append(min(a1, a2, a3, a4))
    return answer