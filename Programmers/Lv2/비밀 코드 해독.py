from itertools import combinations
import math

# 만약 n이 큰 경우, 완탐으로 불가
def get_comb_cnt(n, r):
    if r < 0 or r > n: return 0
    return math.comb(n, r)

def solution(n, q, ans):
    def sol(selected, rejected, idx):
        if len(selected) > 5 or idx > len(q):
            return 0
        if idx == len(q):
            # 남은 숫자 중에서 5개를 채울 수 있는 조합 수 반환
            total_remaining = n - len(selected) - len(rejected)
            need = 5 - len(selected)
            return get_comb_cnt(total_remaining, need)

        current_try = q[idx]
        expected_match = ans[idx]

        # selected에서 이미 일치한 숫자 수
        matched = len(set(current_try) & set(selected))
        if matched > expected_match:
            return 0

        # current_try에서 아직 선택되지 않고 거절도 안 된 숫자들만 필터
        remaining = [x for x in current_try if x not in selected and x not in rejected]

        # 현재 시도에서 더 뽑아야 할 숫자 수
        needed_from_remaining = expected_match - matched
        if needed_from_remaining > len(remaining):
            return 0

        total = 0

        # remaining에서 needed_from_remaining 개수만큼 선택하는 조합을 모두 탐색
        for combo in combinations(remaining, needed_from_remaining):
            new_selected = selected + list(combo)
            new_rejected = rejected + [x for x in remaining if x not in combo]
            total += sol(new_selected, new_rejected, idx + 1)

        return total

    return sol([], [], 0)



# 기존 풀이
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    m = len(q)
    for comb in combinations(range(1, n+1), 5):
        flag = True
        for i in range(m):
            if not flag: break
            cnt = 0
            for el in q[i]:
                if el in comb: cnt += 1
            if cnt != ans[i]: flag = False
        if flag: answer += 1
    return answer