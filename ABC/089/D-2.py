def main():
    H, W, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[] for _ in range(H * W + 1)]
    for h in range(H):
        for w in range(W):
            B[A[h][w]] = (h,w)
    C = []
    for d in range(1,D+1):
        tmp = []
        x, y = B[d]
        pre = 0
        while d <= H * W:
            nx, ny = B[d]
            now = abs(nx - x) + abs(ny - y) + pre
            tmp.append(now)
            pre = now
            x, y = nx, ny
            d += D
        C.append(tmp)
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        index = L % D
        index -= 1
        cnt = L // D
        if L % D == 0:
            cnt -= 1
        ans = C[index][cnt + (R - L) // D] - C[index][cnt]
        print(ans)



if __name__ == "__main__":
    main()