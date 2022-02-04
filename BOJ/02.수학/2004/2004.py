# 조합 0의 개수
import sys
input = sys.stdin.readline

def tc(x):
    cnt = 0
    while x != 0:
        x = x//2
        cnt += x
    return cnt

def fc(x):
    cnt = 0
    while x != 0:
        x = x//5
        cnt += x
    return cnt

n, m = map(int, input().split())

tc_tot = tc(n) - tc(m) - tc(n-m)
fc_tot = fc(n) - fc(m) - fc(n-m)

if tc_tot > fc_tot:
    print(fc_tot)
else:
    print(tc_tot)
