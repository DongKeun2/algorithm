# 히스토그램에서 가장 큰 직사각형

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

while True:
    lst = list(map(int, input().split()))
    if len(lst) == 1 and lst[0] == 0:
        break
    lst.pop(0)

    result = 0
    sol(lst)

    print(result)