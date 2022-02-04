# 소트인사이드

N = int(input())

n_list = [i for i in str(N)]
n_list.sort()
n_list.reverse()

print(''.join(n_list))