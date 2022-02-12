# 직사각형

for _ in range(4):
    arr = []
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        result = 'd'
    elif x2 == x3 or x1 == x4:
        if y2 > y3 and y1 < y4:
            result = 'b'
        elif y2 == y3 or y1 == y4:
            result = 'c'
        else:
            result = 'a'
    elif y2 == y3 or y1 == y4:
        if x3 < x2 and x1 < x4:
            result = 'b'
        elif x1 == x4 or x2 == x3:
            result = 'c'
        else:
            result = 'a'
    else:
        result = 'a'

    print(result)