H, W, N = map(int, input().split())
maps = [input() for i in range(H)]
a = [] * (N + 1)

for i in range(H):
    for j in range(W):
        if maps[i][j] == 'S':
            a.append([i,j])
        for k in range(1,N+1):
            if maps[i][j] == str(k):
                a.append([i,j])

print(a)