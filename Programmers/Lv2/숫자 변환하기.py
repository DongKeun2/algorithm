# dp로 풀이
def solution(x, y, n):
    lst = [-1] * 1000001
    lst[x] = 0
    for i in range(1000001):
        if lst[i] != -1:
            if i+n <= 1000000:
                if lst[i+n] == -1:
                    lst[i+n] = lst[i] + 1
                else:
                    lst[i+n] = min(lst[i+n], lst[i] + 1)
            if i*2 <= 1000000:
                if lst[i*2] == -1:
                    lst[i*2] = lst[i] + 1
                else:
                    lst[i*2] = min(lst[i*2], lst[i] + 1)
            if i*3 <= 1000000:
                if lst[i*3] == -1:
                    lst[i*3] = lst[i] + 1
                else:
                    lst[i*3] = min(lst[i*3], lst[i] + 1)
    answer = lst[y]
    return answer