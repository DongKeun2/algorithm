# 정식이의 은행업무

def check(x, y):
    global result, flag

    if x == y:
        result = x
        flag = 1
        return


def sol(x, i):
    global flag

    if i >= len(n3):
        return

    elif flag:
        return

    if n3[-(i+1)] == '0':
        check(x, num3 + tmp3[i])
        check(x, num3 + 2 * tmp3[i])
    elif n3[-(i+1)] == '1':
        check(x, num3 - tmp3[i])
        check(x, num3 + tmp3[i])
    else:
        check(x, num3 - tmp3[i])
        check(x, num3 - 2 * tmp3[i])

    sol(x, i + 1)


T = int(input())

tmp2 = [2 ** i for i in range(40)]
tmp3 = [3 ** i for i in range(40)]

for test_case in range(1, T + 1):
    n2 = input()
    n3 = input()

    num2 = 0
    for i in range(len(n2))[::-1]:
        if n2[i] == '1':
            num2 += 2 ** (len(n2) - i - 1)

    num3 = 0
    for i in range(len(n3))[::-1]:
        if n3[i] != '0':
            num3 += int(n3[i]) * 3 ** (len(n3) - i - 1)

    flag = 0
    for i in range(len(n2)):
        if flag:
            break

        if n2[-(i + 1)] == '1':
            x = num2 - tmp2[i]
        else:
            x = num2 + tmp2[i]

        sol(x, 0)

    print(f'#{test_case} {result}')