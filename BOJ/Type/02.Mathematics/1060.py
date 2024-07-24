# 좋은 수 / 골드1
# 수학, 자료 구조, 정렬, 우선순위 큐

from heapq import heappush, heappop

L = int(input())
lst = [0]+list(map(int, input().split()))
n = int(input())
lst.sort()

heap = []
heappush(heap, (lst[1]-1, 1, 0, 1))
for i in range(1, L+1):
    heappush(heap, (1, lst[i], i, 0))
    heappush(heap, (lst[i] - lst[i-1] - 1, lst[i]-1, i, -1))
    if i < L: heappush(heap, (lst[i+1] - lst[i] - 1, lst[i]+1, i, 1))

result = []
while heap and len(result) < n:
    cnt, num, idx, flag = heappop(heap)
    if 0 < cnt and 0 < num and num not in result:
        heappush(heap, (abs((lst[idx+flag] - (num + flag))*(lst[idx] - (num + flag))), num + flag, idx, flag))
        result.append(num)

print(*(result + [x for x in range(lst[L]+1, lst[L] + n-len(result)+1)])) if len(result) < n else print(*result[:n])