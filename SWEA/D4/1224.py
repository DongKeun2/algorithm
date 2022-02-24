# [SW 문제해결 기본] 6일차 - 계산기3

T = 10

for test_case in range(1, T+1):
    N = int(input())
    S = input()
    tb = ['+', '*', ')', '(']

    # 후위 표기식 변환
    result = ''
    st = []
    for s in S:
        if s in tb:
            if s == '+':
                while st and st[-1] != '(':
                    result += st.pop()
                st.append(s)
            elif s =='*':
                while st and st[-1] == '*':
                    result += st.pop()
                st.append(s)
            elif s == '(':
                st.append(s)
            else:
                while st[-1] != '(':
                    result += st.pop()
                st.pop()
        else:
            result += s
    while st:
        result += st.pop()

    # 후위 표기식 계산
    st = []
    for s in result:
        if s in tb:
            n2 = st.pop()
            n1 = st.pop()
            if s == '+':
                st.append(int(n1)+int(n2))
            else:
                st.append(int(n1)*int(n2))
        else:
            st.append(s)
    result = st[0]

    print(f'#{test_case} {result}')
    