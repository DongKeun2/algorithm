# 쿠키 구입 Lv4
# Summer/Winter Coding(~2018)

# 첫째 기준으로 시작
# 값 비교 후 더 작은 값에 더해주는 식으로 진행
# 같은 값이라면 answer 갱신
def solution(cookie):
    n = len(cookie)
    answer = 0
    for l in range(n-1):
        r = l + 1
        a = cookie[l]
        b = cookie[r]
        while True:
            if a == b:
                answer = max(answer, a)
            
            if a >= b and r < n-1:
                r += 1
                b += cookie[r]
            elif a <= b and l > 0:
                l -= 1
                a += cookie[l]
            else:
                break
                    
    return answer