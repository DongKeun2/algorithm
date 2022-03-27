# BFS 스페셜 저지
from collections import deque
import sys
input = sys.stdin.readline

# 입력받은 순서가 bfs로 탐색할 때 가능한 순서인지 확인
def sol2():
    global result

    # cnt1을 지나 cnt 2부터 확인.
    # lst의 인덱스 idx
    # cnt의 인덱스 flag
    idx = 1
    flag = 2

    # 가능한 순서인지 확인하기 위한 q
    q= deque([])
    q.append(1)

    while True:
        # 순서대로 출력이 가능하다면 종료
        if idx >= len(lst):
            return

        # cnt[flag]를 비웠다면 다음 확인
        # ex) cnt[2] = [2, 3] 에서 2와 3을 확인후에 제거 => cnt[3] 확인
        if flag <= N and cnt[flag] == []:
            flag += 1

        # cnt 순서에 따라 확인하므로 이번에 확인할 수가 현재 cnt안에 있는 지 확인
        elif lst[idx] in cnt[flag]:

            # 만약 3를 확인하고자한다면 q에는 1과 2저장
            if q:
                # 1에 3이 연결되어 있으므로 q에 3 저장, cnt에서 3 제거, 다음 수를 확인하기 위해 idx +1
                if lst[idx] in arr[q[0]]:
                    q.append(lst[idx])
                    cnt[flag].remove(lst[idx])
                    idx += 1

                # 만약 4를 확인한다면 q에는 1,2,3 저장
                # 4는 1에 연결되어 있지않지만 1, 2, 3, 4는 가능한 순서
                # 4가 연결된 정점이 p[0]에 올때까지 popleft 
                else:

                    # 4와 연결된 숫자가 있을때까지 q에서 제거
                    while q:
                        q.popleft()
                        if q and lst[idx] in arr[q[0]]:
                            q.append(lst[idx])
                            cnt[flag].remove(lst[idx])
                            idx += 1
                            break

            # q가 비워져있다면 실패
            else:
                result = 0
                return

        # 현재 확인해야하는 정점이 cnt에 없다면 실패
        else:
            result = 0
            return


# 각 정점의 방문 가능한 순서 cnt 저장, 항상 cnt[1] = [1]
# ex) 예제 1번의 경우 cnt[2] = [2, 3]
def sol(s):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        n = vst[s]
        for x in arr[s]:
            if vst[x] == 0:
                vst[x] = n+1
                cnt[n+1].append(x)
                q.append(x)
    return


N = int(input())

# 인접리스트 만들기
arr =[[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 문제에서 입력받는 순서
lst = list(map(int, input().split()))

# 시작 순서가 1이 아니라면 안된다.
if lst[0] != 1:
    result = 0
else:
    cnt = [[] for _ in range(N+1)]
    cnt[1].append(1)
    vst = [0] * (N+1)
    vst[1] = 1
    sol(1)

    result = 1
    sol2()
    

print(result)
