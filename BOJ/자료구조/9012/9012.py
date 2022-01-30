# 괄호

T = int(input())

for _ in range(T):

    ps = input()

    vps = []
    for s in ps:
        if s == '(':
            vps.append(s)
        else:
            if vps:
                vps.pop()
            else:
                print('NO')
                break
    else:
        if vps:
            print('NO')
        else:
            print('YES')
