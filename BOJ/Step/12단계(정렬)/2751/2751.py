# 수 정렬하기 2

import sys

N = int(input())

N_list = []
for i in range(N):
    N_list.append(int(sys.stdin.readline()))

N_list.sort()
for i in N_list:
    print(i)