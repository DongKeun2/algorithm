# 부분수열의 합 2 / 골드1

def get_nums(lst):
    n = len(lst)
    nums = []
    for i in range(1<<n):
        tmp = []
        for j in range(n):
            if i & (1<<j):
                tmp.append(lst[j])
        if tmp: nums.append(sum(tmp))
    return nums

N, S = map(int, input().split())
arr = list(map(int, input().split()))
left = sorted(get_nums(arr[:N//2]))
right = sorted(get_nums(arr[N//2:]), reverse=True)

ll, lr = len(left), len(right)
li, ri, cnt = 0, 0, 0
while li < ll and ri < lr:
    s = left[li] + right[ri]
    if s < S:
        li += 1
    elif s > S:
        ri += 1
    else:
        lc, rc = 1, 1
        while li + 1 < ll and left[li] == left[li + 1]:
            lc += 1
        while ri + 1 < lr and right[ri] == right[ri + 1]:
            rc += 1
        cnt += lc * rc
        li += lc
        ri += rc
print(cnt)