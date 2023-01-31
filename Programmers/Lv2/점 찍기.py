# 연습문제 Lv2

def solution(k, d):
    # 0,0 과 0, ak인 경우
    answer = (d//k) * 2 + 1

    # ak, bk인 경우
    tmp = k
    dist = d
    while tmp <= dist:
        if tmp ** 2 + dist ** 2 <= d ** 2:
            if (dist - tmp) // k <= 0:
                answer += 1
                return answer
            
            answer += ((dist - tmp) // k)*2 + 1
            tmp += k
        else:
            dist -= 1
    
    return answer