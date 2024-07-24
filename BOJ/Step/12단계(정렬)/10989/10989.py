# 수 정렬하기 3
import sys
input = sys.stdin.readline

N = int(input())

cl = [0]*(10001)
for _ in range(N):
    cl[int(input())] += 1


for i,c in enumerate(cl):
    if c > 0:
        for _ in range(c):
            print(i)
