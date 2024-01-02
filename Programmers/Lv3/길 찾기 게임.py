# 2019 KAKAO BLIND RECRUITMENT 길 찾기 게임 Lv3
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    n = len(nodeinfo)
    # 전위 순회
    # y축 내림차순 정렬
    # root추가 후 좌,우 순으로 재귀
    def find_pre():
        arr = sorted(list(zip(range(1, n+1), nodeinfo)), key = lambda item : -item[1][1])
        pre_answer = []
        def find_fnc(lst):
            left = []
            right = []
            top_idx, [top_x, top_y] = lst.pop(0)
            for idx, [x, y] in lst:
                if top_x < x:
                    right.append((idx, [x,y]))
                else:
                    left.append((idx, [x,y]))
            pre_answer.append(top_idx)
            if left:
                find_fnc(left)
            if right:
                find_fnc(right) 
            return
        find_fnc(arr)
        return pre_answer

    # 후위 순회
    # x축 오름차순 정렬
    # stack (y축 내림차순 정렬) 활용
    def find_post():
        arr = sorted(list(zip(range(1, n+1), nodeinfo)), key = lambda item : item[1][0])
        post_answer = []
        st = []
        for idx, [x, y] in arr:
            while st:
                if st[-1][1] >= y:
                    break
                post_answer.append(st.pop())
            st.append((x,y,idx))
        while st:
            post_answer.append(st.pop())
        return [item[2] for item in post_answer]
    
    answer = [find_pre(), find_post()]
    return answer