# [SW 문제해결 응용] 1일차 - 암호코드 스캔

def sol(code16):
    global result

    code2 = ''
    for n in code16:
        if 65 <= ord(n) <= 90:
            x = ord(n) - 55
        else:
            x = int(n)

        for i in range(4)[::-1]:
            code2 += str(x // (2 ** i))
            x %= 2 ** i

    v = '0'
    code = []
    cnt = 0
    for i in range(len(code2)):
        if code2[i] == v:
            cnt += 1
        else:
            code.append(cnt)
            cnt = 1
            v = code2[i]
    if v == '1':
        code.append(cnt)

    pwd = []
    for i in range(3, len(code), 4)[::-1]:
        if min(code[i-2:i+1]) != 1:
            n = min(code[i-2:i+1])
            for k in range(3):
                code[i-2+k] //= n

        c = ''.join(str(x) for x in code[i-2:i+1])

        for k in range(10):
            if c == key[k]:
                pwd.append(k)
                break

    if len(pwd) >= 8:
        idx = len(pwd)
        while idx > 7:
            tot = 0
            for j in range(idx-8, idx):
                if (j-(idx-8))%2:
                    tot += 3*pwd[j]
                else:
                    tot += pwd[j]

            if tot%10 == 0:
                if pwd[idx-8:idx] not in ans:
                    result += sum(pwd[idx-8:idx])
                    ans.append(pwd[idx-8:idx])
            idx -= 8


T = int(input())

key = [
    '211',
    '221',
    '122',
    '411',
    '132',
    '231',
    '114',
    '312',
    '213',
    '112'
]

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    flag = 0
    for _ in range(N):
        lst = list(input())
        if arr == []:
            arr.append(lst)
        elif arr and lst != arr[-1]:
            arr.append(lst)
    ans = []
    result = 0
    vst = []
    for lst in arr:
        if lst.count('0') != M:
            cnt = 0
            flag = 0
            code16 = []
            for i in range(M):
                if lst[i] != '0':
                    cnt = 0
                    flag = 1
                    code16.append(lst[i])
                elif flag == 1 and lst[i] == '0':
                    cnt += 1
                    code16.append(lst[i])

                    if cnt >= 4:
                        flag = 0
                        if code16 not in vst:
                            sol(code16)
                            vst.append(code16)
                        code16 = []
            if code16 not in vst:
                sol(code16)
                vst.append(code16)

    print(f'#{test_case} {result}')
