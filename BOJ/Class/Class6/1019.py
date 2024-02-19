# 책 페이지 / 골드1
# 수학

N = int(input())

def get_zero_count():
    cnt = 0
    idx = 1
    while N >= 10**idx:
        if idx == 1 or  N // 10**(idx-1) % 10:
            cnt += N // 10**idx * 10 ** (idx-1)
        else:
            cnt += (N // 10**idx -1) * 10**(idx-1) + N % 10**(idx-1) + 1
        idx += 1
    return cnt

def get_count(n):
    cnt = 0
    idx = 1
    while N >= 10**(idx-1):
        cnt += N // 10**idx * 10**(idx-1)
        if N // (10 ** (idx-1)) % 10 >= n:
            if idx == 1:
                cnt += 1
            else:
                if N // (10 ** (idx-1)) % 10 > n:
                    cnt += 10 ** (idx-1)
                if N // (10 ** (idx-1)) % 10 == n:
                    cnt += N % 10 ** (idx-1) + 1
        idx += 1
    return cnt

result = [get_zero_count()]
for i in range(1, 10):
    result.append(get_count(i))
print(*result)