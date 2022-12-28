# 트리
# 30616KB, 36ms

# 루트부터 차례대로 자식 노드 확인
def sol(node):
    global cnt

    # 지워진 노드라면 연결 끊기
    if node == remove:
        return
    
    # 자식 노드가 있다면 재귀
    if tmp[node]:
        for n in tmp[node]:
            # 자식 노드가 지워진 노드라면 제외하고 재귀
            # 자식 리스트에 지워진 노드만 있다면 리프 노드이므로 +1
            if n == remove and len(tmp[node]) == 1:
                cnt += 1
                return
            else:
                sol(n)

    # 자식 노드가 없다면 리프 노드
    else:
        cnt += 1
        return


N = int(input())
lst = list(map(int, input().split()))
remove = int(input())

# 해당 노드의 자식노드 기록할 배열 생성 / 루트 노드 기록
# 지워질 노드는 저장하지 않음
tmp = [[] for _ in range(N)]
for i in range(N):
    if lst[i] == remove:
        continue
    elif lst[i] == -1:
        root = i
    else:
        tmp[lst[i]].append(i)

cnt = 0
sol(root)

print(cnt)