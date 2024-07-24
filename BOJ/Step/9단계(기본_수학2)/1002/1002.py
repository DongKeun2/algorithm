# 터렛

T = int(input())

for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = list(map(int, input().split()))

    a = [x_1, y_1]
    b = [x_2, y_2]
    r = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) **(1/2)
    if a == b:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)
    else:
        if r == r_1 + r_2:
            print(1)
        elif r > r_1 + r_2:
            print(0)
        else:
            if r_1 == r_2:
                print(2)
            elif r_1 > r_2:
                if r + r_2 < r_1:
                    print(0)
                elif r + r_2 == r_1:
                    print(1)
                else:
                    print(2)
            else:
                if r + r_1 < r_2:
                    print(0)
                elif r + r_1 ==  r_2:
                    print(1)
                else:
                    print(2)
