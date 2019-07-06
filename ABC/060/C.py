N, T = map(int, input().split())
t = list(map(int, input().split()))

time = 0

for i in range(N):
    if i + 1 == N:
        time += T
        break
    if t[i+1] - t[i] < T:
        time += (t[i+1] - t[i])
    else:
        time += T
print(time)
