N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

money = -1

for i in s:
    cnt = s.count(i) - t.count(i)
    if money < cnt:
        money = cnt

if money <= 0:
    print(0)
else:
    print(money)