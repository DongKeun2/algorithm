# 2025 프로그래머스 코드챌린지 1차 예선 lv2

from itertools import combinations

def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n-1)

def get_comb_cnt(n, r):
    if r < 0 or r > n: return 0
    return factorial(n) // (factorial(r) * factorial(n-r))

def solution(n, q, ans):
    global answer
    def sol(lst, trash_lst, idx):
        global answer
        if len(lst) > 5:
            return
        if idx >= 5:
            total_num_cnt = n - len(lst), len(trash_lst)
            bonus_cnt = 5 - len(lst)
            answer += get_comb_cnt(total_num_cnt, bonus_cnt)
            return
        
        # lst에 있는 값이 q[idx]에 ans이상 있는 지 확인 후 리턴
        # ans보다 크다면 리턴
        # 같다면 모두 trash에 넣은 후 재귀
        # 부족하다면 ans에 맞춰 조합을 구하여 lst, 나머지는 trash에 넣고 재귀
        ## 이 때 이미 trash에 있는 값은 lst에 넣지 않도록 주의
        for x in combinations(q[idx], ans[idx]):
            return
    
    
    answer = 0
    sol([], [], 0)
    return answer
n1 = 10
q1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans1 = 	[2, 3, 4, 3, 3]

n2 =15
q2 = [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]
ans2 = [2, 1, 3, 0, 1]
solution(n1, q1, ans1)