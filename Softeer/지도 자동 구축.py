# 지도 자동 구축 Lv2

import sys
input = sys.stdin.readline

# 점의 개수는 한 변에 존재하는 점의 개수의 제곱
# 매 단계마다 가로와 세로선은 점의 개수-1만큼 늘어남
N = int(input())
lst = [0] * 16
lst[0] = 2
for i in range(1, 16):
    lst[i] = 2*lst[i-1] -1
    
print(lst[N]**2)