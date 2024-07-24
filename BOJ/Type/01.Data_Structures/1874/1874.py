# 스택 수열

import sys
input = sys.stdin.readline

n = int(input())

st = []
cnt = 1
cnt_st = []
for _ in range(n):
    m = int(input())
    
    while m >= cnt:
        st.append(cnt)
        cnt_st.append('+')
        cnt += 1
    
    if m not in st:
        print('NO')
        break
    else:    
        while m in st:
            st.pop()
            cnt_st.append('-')
else:
    for x in cnt_st:
        print(x)

