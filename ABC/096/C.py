H,W = map(int, input().split())

S = [list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue

        cnt = 0
        for dy in [-1,1]:
            if 0 <= i + dy < H:
                if S[i+dy][j] == '#':
                        cnt += 1
        for dx in [-1,1]:
            if 0 <= j + dx < W:
                if S[i][j+dx] == '#':
                    cnt += 1
        if cnt == 0:
            print('No')
            exit()

print('Yes')