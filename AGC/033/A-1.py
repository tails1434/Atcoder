def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    d = [[0] * W for _ in range(W)]
    for h in range(H):
        cnt = 0
        flag = False
        for w in range(W):
            if A[h][w] == '#':
                flag = True
                cnt = 1
                continue
            if flag:
                if d[h][w]:
                    d[h][w] = min(d[h][w],cnt)
                else:
                    d[h][w] = cnt
                cnt += 1
    for h in range(H):
        cnt = 0
        flag = False
        for w in range(W-1,-1,-1):
            if A[h][w] == '#':
                flag = True
                cnt = 1
            if flag:
                if d[h][w]:
                    d[h][w] = min(d[h][w],cnt)
                else:
                    d[h][w] = cnt
                cnt += 1
    
    for w in range(W):
        cnt = 0
        flag = False
        for h in range(H):
            if A[h][w] == '#':
                flag = True
                cnt = 1
                continue
            if flag:
                if d[h][w]:
                    d[h][w] = min(d[h][w],cnt)
                else:
                    d[h][w] = cnt
                cnt += 1
    for w in range(W):
        cnt = 0
        flag = False
        for h in range(H-1,-1,-1):
            if A[h][w] == '#':
                flag = True
                cnt = 1
                continue
            if flag:
                if d[h][w]:
                    d[h][w] = min(d[h][w],cnt)
                else:
                    d[h][w] = cnt
                cnt += 1
    for h in range(H):
        for w in range(W-1):    
    ans = 0
    print(d)
    for h in range(H):
        ans = max(max(d[h]),ans)

    print(ans)

if __name__ == "__main__":
    main()