def main():
    H, W = map(int, input().split())
    ans = float('inf')
    h1, h2, h3 = 0,0,0
    w1,w2,w1 = 0,0,0
    # 横3に切る場合
    h1 = H // 3
    h2 = H // 3
    h3 = H // 3
    if H % 3 == 1:
        h3 += 1
    elif H % 3 == 2:
        h2 += 1
        h3 += 1
    S = [h1*W,h2*W,h3*W]
    ans = min(max(S)-min(S),ans)
    # 横2縦1に切る場合
    h1 = H // 2
    h2 = H // 2
    h3 = H
    if H % 2 == 1:
        h2 += 1
    for w in range(1,W):
        S = [h1*(W-w),h2*(W-w),h3*w]
        ans = min(max(S)-min(S),ans)
    # 縦3に切る場合
    w1 = W // 3
    w2 = W // 3
    w3 = W // 3
    if W % 3 == 1:
        w3 += 1
    elif W % 3 == 2:
        w2 += 1
        w3 += 1
    S = [w1*H,w2*H,w3*H]
    ans = min(max(S)-min(S),ans)

    # 縦2横1に切る場合
    w1 = W // 2
    w2 = W // 2
    w3 = W
    if W % 2 == 1:
        w2 += 1
    for h in range(1,H):
        S = [w1*(H-h),w2*(H-h),w3*h]
        ans = min(max(S)-min(S),ans)

    print(ans)

if __name__ == "__main__":
    main()