# 줄 세우기
# 구현 시뮬레이션

P = int(input())

for test_case in range(1, P+1):
    lst = list(map(int, input().split()))

    result = 0
    for i in range(1, len(lst)-1):
        n = lst[i]
        idx = i
        for j in range(i, len(lst)):
            if n > lst[j]:
                n = lst[j]
                idx = j
        lst.pop(idx)
        lst.insert(i, n)
        result += (idx - i)

    print(test_case, result)