# 유사 칸토어 비트열 Lv2 (체감 Lv4)
# 연습문제

# 5의 idx승에는 4의 idx승만큼의 1이 존재한다.
# x//x를 넘지않는 5의 제곱수 == 2 구간에는 0만 존재한다.
def cnt(x):
    if x <= 5:
        if x > 2:
            return x-1
        return x
    
    idx = 1
    while x > 5**(idx+1):
        idx+=1
    
    return 4**(idx) * cnt(x//(5**idx)) + (cnt(x%(5**idx)) if x//(5**idx) != 2 else 0)
    

def solution(n, l, r):
    answer = cnt(r) - cnt(l-1)
    return answer
