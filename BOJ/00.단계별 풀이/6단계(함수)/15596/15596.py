# 정수 N개의 합

def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
X = list(map(int,input().split()))
print(solve(X))