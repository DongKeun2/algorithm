# 이진 검색 트리
# 448140KB, 3592ms

import sys
sys.setrecursionlimit(10**6)

# 좌, 우로 나눠서 재귀
def sol(tree):
    root = tree[0]
    left = []
    right = []

    # 루트 노드보다 작으면 왼쪽, 크면 오른쪽에 저장
    for node in tree:
        if node < root:
            left.append(node)
        elif node > root:
            right.append(node)

    # 왼쪽부터 재귀
    if left:
        sol(left)
    if right:
        sol(right)
    
    # 좌, 우 보내고 난 뒤 루트 노드 출력
    print(root)
    return

# tmp에 전위 순회 결과 순서대로 저장
tmp = []
while True:
    try:
        num = int(input())
        tmp.append(num)
    except:
        break

sol(tmp)