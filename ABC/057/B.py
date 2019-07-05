N, M = map(int, input().split())

a = [0] * N
b = [0] * N
c = [0] * M
d = [0] * M
for _ in range(N):
    a[_], b[_] = map(int, input().split())

for _ in range(M):
    c[_], d[_] = map(int, input().split())


for i in range(N):
    min_dist = float('inf')
    ans = 0
    for j in range(M):
        distance = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if min_dist > distance:
            min_dist = distance
            ans = j + 1
    print(ans)