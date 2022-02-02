# 접미사 배열

S = input()

result = []
for i in range(len(S)):
    result.append(S[i:])

result.sort()

for i in range(len(result)):
    print(result[i])