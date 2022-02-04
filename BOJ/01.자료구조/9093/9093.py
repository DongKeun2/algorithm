# 단어 뒤집기
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sent = list(map(str, input().split()))
    s_list = []
    for s in sent:
        s_list.append(''.join(reversed(s)))

    print(*s_list)
