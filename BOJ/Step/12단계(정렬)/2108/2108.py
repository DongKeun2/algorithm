# 통계학
import sys
input = sys.stdin.readline

N = int(input())

nl = []
for _ in range(N):
    nl.append(int(input()))

print(round(sum(nl)/len(nl)))
print(sorted(nl)[int(len(nl)/2)])

cl = [0] * 8001

for n in nl:
    cl[n+4000] += 1

mc = max(cl)
cnt = 0
for i in range(len(cl)):
    if cl[i] == mc:
        cnt += 1
        mi = i
        if cnt >= 2:
            break
    
print(mi-4000)

print(max(nl)-min(nl))