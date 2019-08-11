N = input()
fx = 0
for n in N:
    fx += int(n)

if int(N) % fx == 0:
    print('Yes')
else:
    print('No')