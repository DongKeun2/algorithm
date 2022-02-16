# 방 배정
import math

N, K = map(int, input().split())

sd = {
    (0,1) : 0,
    (0,2) : 0,
    (0,3) : 0,
    (0,4) : 0,
    (0,5) : 0,
    (0,6) : 0,
    (1,1) : 0,
    (1,2) : 0,
    (1,3) : 0,
    (1,4) : 0,
    (1,5) : 0,
    (1,6) : 0,
}

for _ in range(N):
    S, Y = map(int, input().split())
    sd[(S,Y)] = sd[(S,Y)] + 1

result = 0
for s in sd.values():
    result += math.ceil(s/K)

print(result)