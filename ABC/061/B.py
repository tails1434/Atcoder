N, M = map(int, input().split())

a = [0] * M
b = [0] * M
for i in range(M):
    a[i],b[i] = map(int, input().split())

for i in range(1, N+1):
    print(a.count(i) + b.count(i))