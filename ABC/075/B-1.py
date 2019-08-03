H, W = map(int, input().split())
S = [list(input()) for i in range(H)]


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        cnt = 0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if 0 <= i + dx < H and 0 <= j + dy < W:
                    if S[i+dx][j+dy] == "#":
                        cnt += 1
                else:
                    continue
        S[i][j] = str(cnt)

for k in S:
    print("".join(k))