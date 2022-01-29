# 수도 요금 경쟁


def chip_p(p, q, r, s, w):
    
    pa = w*p

    if r < w:
        pb = q + (w-r)*s

    else:
        pb = q

    if pb > pa:
        return pa
    return pb



T = int(input())

for i in range(1, T+1):

    p, q, r, s, w = list(map(int, input().split()))

    print(f'#{i} {chip_p(p, q, r, s, w)}')
