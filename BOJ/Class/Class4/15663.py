# N과 M (9) / 실버2

from itertools import permutations

N, M = map(int, input().split())
for lst in sorted(list(set(permutations(map(int, input().split()), M)))): print(*lst)