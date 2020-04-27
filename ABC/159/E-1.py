def main():
    H, W, K = map(int, input().split())
    S = [list(map(int,list(input()))) for _ in range(H)]
    
    ans = float('inf')
    for i in range(1<<H-1):
        cut = []
        for j in range(H):
            if (i >> j) & 1:
                cut.append(j+1)

        tmp_S = [[0] * W for _ in range(len(cut) + 1)]
        tmp_id = 0
        for i in range(H):
            if i in cut:
                tmp_id += 1
            for j in range(W):
                tmp_S[tmp_id][j] += S[i][j]
        
        isOK = True
        for i in range(len(cut) + 1):
            for w in range(W):
                if tmp_S[i][w] > K:
                    isOK = False

        if not isOK:
            continue

        cnt = len(cut)
        white = [0] * (len(cut)+1)

        flag = False
        for w in range(W):
            for i in range(len(cut) + 1):
                white[i] += tmp_S[i][w]
                if white[i] > K:
                    cnt += 1
                    flag = True
                    break
            if flag:
                for i in range(len(cut) + 1):
                    white[i] = tmp_S[i][w]
                flag = False
        ans = min(ans, cnt)

    print(ans)

                


if __name__ == "__main__":
    main()