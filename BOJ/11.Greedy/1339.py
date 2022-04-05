# 단어 수학
# 그리디, 브루트 포스

N = int(input())

arr = []
for _ in range(N):
    arr.append(input())

dct = {}
for lst in arr:
    for i in range(len(lst))[::-1]:
        if dct.get(lst[i]) == None:
            dct[lst[i]] = 10**(len(lst)-i-1)
        else:
            dct[lst[i]] = dct.get(lst[i]) + 10**(len(lst)-i-1)
    
nums = []
for key, value in dct.items():
    nums.append([value, key])
nums.sort()

n = 9
dct = {}
for num in nums[::-1]:
    dct[num[1]] = n
    n -= 1

result = 0
for lst in arr:
    tot = ''
    for s in lst:
        tot += str(dct[s])
    result += int(tot)

print(result)