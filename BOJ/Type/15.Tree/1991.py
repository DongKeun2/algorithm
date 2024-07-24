# 트리 순회

def sol(v):
    global result1, result2, result3

    # 자식이 .이 아니라면 동작
    if v != '.':
        # 전위순회 (VLR)
        result1 += v
        sol(ch1[tree.get(v)])
        # 중위순회 (LVR)
        result2 += v
        sol(ch2[tree.get(v)])
        # 후위순회 (LRV)
        result3 += v


N = int(input())

# 노드 딕셔너리로 저장 ex) A : 0
# 좌, 우 자식 ch1,2에 각각 저장
tree = {}
ch1 = []
ch2 = []
for i in range(N):
    a, b, c = map(str, input().split())
    tree[a] = i
    ch1.append(b)
    ch2.append(c)

# 전위 중위 후위 순회 결과값
result1 = ''
result2 = ''
result3 = ''
sol('A')

print(result1)
print(result2)
print(result3)
