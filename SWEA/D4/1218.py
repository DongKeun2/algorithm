# [SW 문제해결 기본] 4일차 - 괄호 짝짓기

T = 10
for test_case in range(1, T+1):
    N = int(input())
    S = input()

    o = ['(', '[', '{', '<']
    c = [')', ']', '}', '>']
    st = []
    result = 1
    for s in S:
        if result == 0:
            break
        if s in o:
            st.append(s)
        else:
            for i in range(4):
                if s == c[i]:
                    if st[-1] == o[i]:
                        st.pop()
                    else:
                        result = 0
                        break
    
    if st:
        result = 0
    
    print(f'#{test_case} {result}')
