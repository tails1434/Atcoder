x = int(input())

cnt = 0
if x % 11 == 0:
    cnt = (x // 11) * 2
elif 1 <= x % 11 <= 6:
    cnt = (x // 11) * 2 + 1
elif 7 <= x % 11 <= 10:
    cnt = (x // 11) * 2 + 2

print(cnt)