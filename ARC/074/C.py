def main():
    H, W = map(int, input().split())
    S = H * W
    ans = float('inf')
    for h1 in range(1,H):
        S1 = h1 * W
        # 縦に分割する場合
        h2 = (H - h1) // 2
        S2 = h2 * W
        S3 = (H - h1 - h2) * W
        ans = min(ans, max(S1,S2,S3) - min(S1,S2,S3))
        # 横に分割する場合
        w2 = W // 2
        w3 = W - w2
        S2 = (H - h1) * w2
        S3 = (H - h1) * w3
        ans = min(ans, max(S1,S2,S3) - min(S1,S2,S3))

    for w1 in range(1,W):
        S1 = w1 * H
        # 横に分割する場合
        w2 = (W - w1) // 2
        S2 = w2 * H
        S3 = (W - w1 - w2) * H
        ans = min(ans, max(S1,S2,S3) - min(S1,S2,S3))
        # 縦に分割する場合
        h2 = H // 2
        h3 = H - h2
        S2 = (W - w1) * h2
        S3 = (W - w1) * h3
        ans = min(ans, max(S1,S2,S3) - min(S1,S2,S3))

    print(ans)


    
    

if __name__ == "__main__":
    main()