#方針 N人に配っても余っている場合は一人にすべて押し付けることで最大値を求める


N, x = map(int, input().split())
a = list(map(int, input().split()))

sort_a = sorted(a)

cnt = 0
sum_a = 0
for i in sort_a:
    x -= i
    if x >= 0:
        cnt += 1
    else:
        break

if x > 0:
    cnt -= 1

print(cnt)
