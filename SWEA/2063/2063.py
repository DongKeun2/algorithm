# 중간값 찾기

N = int(input())
numbers = list(map(int,input().split()))

new_list = []

for i in range(len(numbers)):
    min_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
        else:
            continue
    new_list.append(min_num)
    numbers.remove(min_num)

median_num = new_list[int(len(new_list)/2)]

print(median_num)