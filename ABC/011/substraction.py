N = int(input())
NG = [int(input()) for _ in range(3)]

if N in NG:
    print('NO')
    exit()

for i in range(100):
    if N - 3 not in NG:
        N = N - 3
    elif N - 2 not in NG:
        N = N - 2
    elif N - 1 not in NG:
        N = N - 1
    else:
        print('NO')
        exit()
else:
    if N <= 0:
        print('YES')
    else:
        print('NO')