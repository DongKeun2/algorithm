# 히스토그램 / 플레티넘5

def sol(lst):
    global result

    st = []
    for i in range(len(lst)):
        while st and lst[st[-1]] >= lst[i]:
            idx = st.pop()
            if st:
                result = max(result, lst[idx] * (i-st[-1]-1))
            else:
                result = max(result, lst[idx] * i)
        st.append(i)
    
    while st:
        idx = st.pop()
        if st:
            result = max(result, lst[idx] * (len(lst) - st[-1] - 1))
        else:
            result = max(result, lst[idx] * len(lst))

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

result = 0
sol(lst)

print(result)