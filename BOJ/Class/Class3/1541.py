# 잃어버린 괄호, 실버2

arr = input().strip().split('-')

answer = 0
for x in arr.pop(0).split('+'):
    answer += int(x)
for st in arr:
    tmp = 0
    lst = st.split('+')
    for x in lst:
        tmp += int(x)
    answer -= tmp
print(answer)


