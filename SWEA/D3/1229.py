# [SW 문제해결 기본] 8일차 -암호문2

T = 10
for test_case in range(1, T+1):
    N = int(input())
    result = list(map(int, input().split()))
    C = int(input())
    lst = list(input().split())

    st = []
    for i in range(len(lst)):
        if i == 0:
            st.append(lst[i])
        else:
            if lst[i] == 'I' or lst[i] == 'D':
                if st[0] == 'I':
                    while len(st) > 3:
                        result.insert(int(st[1]), st.pop())
                    st = [lst[i]]
                elif st[0] == 'D':
                    for _ in range(int(st[2])):
                        result.pop(int(st[1]))
                    st = [lst[i]]
            else:
                st.append(lst[i])

    if st[0] == 'I':
        while len(st) > 3:
            result.insert(int(st[1]), st.pop())
    elif st[0] == 'D':
        for _ in range(int(st[2])):
            result.pop(int(st[1]))

    print(f'#{test_case}', *result[:10])