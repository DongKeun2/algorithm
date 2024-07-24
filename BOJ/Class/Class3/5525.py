# IOIOI, 실버1

N = int(input())
S = int(input())
st = input().strip()

flag = False    # I로 시작하는지
cnt = 0         # IOIOIO.. 형태의 문자열 길이
lst = []        # cnt 저장
for s in st:
    if s == 'I':
        if cnt % 2 == 0: cnt += 1
        elif cnt >= 3: lst.append(cnt)
        else: cnt = 1
        flag = True
    else:
        if flag and cnt % 2: cnt += 1
        elif cnt >= 3: lst.append(cnt - 1)
        else:
            cnt = 0
            flag = False
if s == 'O': lst.append(cnt-1)
elif cnt >= 3: lst.append(cnt)
print(sum([n//2 + 1 - N if n//2 >= N else 0 for n in lst]))