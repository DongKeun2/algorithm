# 점프와 순간 이동 Lv2
# Summer/Winter Coding(~2018)

# Greedy 풀이
def solution(n):
    ans = 1
    # 2로 나누어지는 수라면 계속해서 순간이동
    # 나누어 지지 않는 수라면 1칸 점프 후 순간이동
    while n > 1:
        ans += n%2
        n //= 2
    return ans