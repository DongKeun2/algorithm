# [인증평가(5차) 기출] 업무 처리
# 난이도3/5

import sys
input = sys.stdin.readline

H, K, R = map(int, input().split())

left = [[] for _ in range(2**(H+1) - 1)]
right = [[] for _ in range(2**(H+1) - 1)]

for i in range(2**H):
    lst = list(map(int, input().split()))
    for leaf in range(K):
        if leaf%2:
            right[2**(H+1) - 2**H - 1 + i].append(lst[leaf])
        else:
            left[2**(H+1) - 2**H - 1 + i].append(lst[leaf])

day = 0
result = 0
while day < R:
    day += 1
    if day%2 and left[0]:
        result += left[0].pop(0)
    elif not day%2 and right[0]:
        result += right[0].pop(0)

    for node in range(1, 2**(H+1) -1):
        p = (node-1)//2
        # 왼쪽에서 쌓인 업무 올리기
        if day%2 and left[node]:
            task = left[node].pop(0)
            # 왼쪽 노드
            if node%2:
                left[p].append(task)
            # 오른쪽 노드
            else:
                right[p].append(task)

        # 오른쪽에서 쌓인 업무 올리기
        elif not day%2 and right[node]:
            task = right[node].pop(0)
            if node%2:
                left[p].append(task)
            else:
                right[p].append(task)

print(result)