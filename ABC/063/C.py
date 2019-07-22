N = int(input())
s = [0] * N
for i in range(N):
    s[i] = int(input())

sum_s = sum(s)
sort_s = sorted(s)

if sum_s % 10 != 0:
    print(sum_s)
else:
    for i in sort_s:
        if i % 10 == 0:
            continue
        else:
            print(sum_s - i)
            exit()
    print(0)