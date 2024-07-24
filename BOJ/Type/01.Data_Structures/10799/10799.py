# 쇠막대기

s = input()

cnt = 0
res = 0
for i in range(len(s)):
    if s[i] == '(':
        cnt += 1
    else:
        if s[i-1] == ')':
            res += 1
            cnt -= 1

        else:
            cnt -= 1
            res += cnt

print(res)
