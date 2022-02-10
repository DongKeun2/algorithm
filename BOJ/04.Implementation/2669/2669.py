# 직사각형 네개의 합집합의 면적 구하기

area = 0
set_s = set()
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            set_s.add((i, j))

area = list(set_s)

print(len(area))