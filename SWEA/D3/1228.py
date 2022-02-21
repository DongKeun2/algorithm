# [SW 문제해결 기본] 8일차 - 암호문1

T = 10
for test_case in range(1, T+1):
    n = int(input())
    result = list(map(int, input().split()))

    m = int(input())
    lst = list(map(str, input().split()))

    arr = []
    st = []
    for i in range(len(lst)):
        if lst[i] == 'I':
            if i != 0 and st:
                arr.append(st)
                st = []
        else:
            st.append(int(lst[i]))

    if st:
        arr.append(st)

    for i in range(len(arr)):
        if arr[i][0] < 10:
            for j in range(2, len(arr[i])):
                result.insert(arr[i][0], arr[i].pop())

    print(f'#{test_case}', *result[:10])
    