N = int(input())
a = list(map(int, input().split()))

sort_a = sorted(a, reverse=True)

sum_team = 0
for i in range(1, 2 * N + 1 ,2):
    sum_team += sort_a[i]

print(sum_team)