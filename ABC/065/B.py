N = int(input())
a = list(int(input()) for i in range(N))

tmp = 1

for i in range(N):
    tmp = a[tmp-1]
    if tmp == 2:
        print(i + 1)
        exit()

print(-1)