# 제로
# 구현 자료구조 스택

K = int(input())
st = []

for i in range(K):
    n = int(input())
    if n == 0:
        st.pop()
    else:
        st.append(n)

print(sum(st))