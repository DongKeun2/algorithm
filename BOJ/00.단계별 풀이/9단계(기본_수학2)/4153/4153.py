# 직각삼각형

while True:
    a, b, c = list(map(int, input().split()))
    list_x = [a, b, c]
    if list_x == [0, 0, 0]:
        break
    z = max(list_x)
    list_x.remove(max(list_x))

    if (list_x[0]**2 + list_x[1] **2)**(1/2) == z:
        print('right')
    else: print('wrong')