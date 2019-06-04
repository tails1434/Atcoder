H, W = map(int, input().split())

S = [list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        cnt = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= i + dy < H and 0 <= j + dx < W:
                    if S[i+dy][j+dx] == '#':
                        cnt += 1
                else:
                    continue
        S[i][j] = str(cnt)

for k in S:
    print("".join(k))