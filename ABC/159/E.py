def main():
    H, W, K = map(int, input().split())
    S = [list(map(int, list(input()))) for _ in range(H)]
    ans = float('inf')
    for i in range(2 ** (H - 1)):
        group = 0
        h_id = [0] * H
        for j in range(H):
            h_id[j] = group
            if i >> j & 1:
                group += 1
        
        group += 1
        c = [[0] * W for _ in range(group)]
        for h in range(H):
            for w in range(W):
                c[h_id[h]][w] += S[h][w]
        g_flag = True
        for g in range(group):
            for w in range(W):
                if c[g][w] > K:
                    g_flag = False

        if not g_flag:
            continue

        cnt = group - 1
        now = [0] * group
        flag = True
        for w in range(W):
            for g in range(group):
                now[g] += c[g][w]
                if now[g] > K:
                    flag = False
                    cnt += 1
                    break
            
            if not flag:
                for g in range(group):
                    now[g] = c[g][w]
                flag = True
        ans = min(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()