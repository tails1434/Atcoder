N = int(input())
A = list(map(int, input().split()))

odd_cnt = 0
four_times_cnt = 0
two_times_cnt = 0
for a in A:
    if a % 2 == 1:
        odd_cnt += 1
    elif a % 4 == 0:
        four_times_cnt += 1
    elif a % 2 == 0:
        two_times_cnt += 1

if two_times_cnt >= 1:
    if odd_cnt <= four_times_cnt:
        print('Yes')
    else:
        print('No')
else:
    if odd_cnt <= four_times_cnt + 1:
        print('Yes')
    else:
        print('No')

