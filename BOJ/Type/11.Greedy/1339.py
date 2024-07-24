# 단어 수학
# 그리디, 브루트 포스

N = int(input())

arr = []
for _ in range(N):
    arr.append(input())

# 각 알파벳 별 우선순위 구하기
dct = {}
for lst in arr:
    for i in range(len(lst))[::-1]:
        if dct.get(lst[i]) == None:
            dct[lst[i]] = 10**(len(lst)-i-1)
        else:
            dct[lst[i]] = dct.get(lst[i]) + 10**(len(lst)-i-1)

# 딕셔너리 => 리스트 ([우선순위, 알파벳])으로 변경
nums = []
for key, value in dct.items():
    nums.append([value, key])
nums.sort()

# 리스트 => 딕셔너리로 변경 (우선순위가 높은 알파벳 9부터 저장)
n = 9
dct = {}
for num in nums[::-1]:
    dct[num[1]] = n
    n -= 1

# 단어를 수로 바꿔서 더해주기
result = 0
for lst in arr:
    tot = ''
    for s in lst:
        tot += str(dct[s])
    result += int(tot)

print(result)