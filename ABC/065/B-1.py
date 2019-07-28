N = int(input())
a = [0] * N
for i in range(N):
    a[i] = int(input())


tmp = 1
for i in range(N):
    tmp = a[tmp-1]
    if tmp == 2:
        print(i + 1)
        exit()

print(-1)