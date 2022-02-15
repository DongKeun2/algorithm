# 다트 게임
# ㅡㅡ

def score(x, y):
    r = (x**2 + y**2)**(1/2)
    for i in range(len(s)-1):
        if r <= s[i]:
            return 10-i
    else:
        return 0


T = int(input())

s = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
for test_case in range(1, T+1):
    n = int(input())

    result = 0
    for _ in range(n):
        x, y = map(int, input().split())
        result += score(x,y)
    
    print(f'#{test_case} {result}')
