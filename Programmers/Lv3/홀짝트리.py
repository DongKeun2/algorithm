# 2025 프로그래머스 코드챌린지 1차 예선

def solution(nodes, edges):
    # 간선 정보 저장
    arr = [[] for _ in range(max(nodes)+1)]
    for s,e in edges:
        arr[s].append(e)
        arr[e].append(s)

    # 해당 노드가 자식 노드인 경우, 홀짝 트리 or 역홀짝 트리인지 구분
    ## lst[n]이 1이면 홀짝 트리
    ## lst[n]이 -1이면 역홀짝 트리
    lst = [0] * (max(nodes)+1)
    for n in nodes:
        if n % 2 == (len(arr[n])-1) % 2: lst[n] = 1
        else: lst[n] = -1

    # 하나의 트리는 홀짝 트리 또는 역홀짝 트리 둘 중 하나
    ## 예외는 각각 홀짝 트리, 역홀짝 트리를 만족하는 2개의 노드로 이루어진 트리
    vst = [0] * (max(nodes)+1)
    answer = [0, 0]
    for n in nodes:
        if vst[n]: continue
        q= [(n, 0)]
        a, b = 0, 0
        while q:
            s, p = q.pop()
            vst[s] = 1
            if lst[s] == 1: a += 1
            else: b += 1
            for e in arr[s]:
                if e != p: q.append((e, s))
        # 트리 내에 홀짝 트리 노드가 하나라면 이 노드가 루트일 때 역홀짝트리
        # 홀짝 트리는 그 반대의 경우
        if a == 1: answer[1] += 1
        if b == 1: answer[0] += 1
    return answer