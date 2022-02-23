# 길찾기

T = 10
for test_case in range(1, T+1):
    tc, n = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = [[0 for _ in range(100)] for _ in range(100)]
    vst = [0 for _ in range(100)]

    for i in range(0, len(lst), 2):
        s = lst[i]
        d = lst[i+1]
        arr[s][d] = 1

    s = 0
    st = [0]
    vst[0] = 1
    while st and s != 99:
        for d in range(0, 100):
            if vst[d] == 0:
                if arr[s][d] == 1:
                    s = d
                    vst[s] = 1
                    st.append(s)
                    break
        else:
            s = st.pop()

    if s == 99:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')
