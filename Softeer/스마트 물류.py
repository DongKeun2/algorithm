# 스마트 물류 Lv3

import sys
input = sys.stdin.readline

# 부품 기준 집을 수 있는 로봇 중 가장 왼쪽의 로봇이 집게한다.
N, K = map(int, input().split())
S = input().strip()
result = 0

vst = [0] * N
for i in range(N):
    if S[i] == 'H':
        for j in range(i-K, i+K+1):
            if 0<= j < N:
                if S[j] == 'P' and vst[j] == 0:
                    result += 1
                    vst[j] = 1
                    break

print(result)