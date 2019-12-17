def main():
    H, W, K = map(int, input().split())
    S = []
    for _ in range(H):
        s = input()
        S.append(s)

    cnt = 0
    ans = [[0] * W for _ in range(H)]
    for h in range(H):
        flag = False
        for w in range(W):
            if flag:
                ans[h][w] = cnt
            if S[h][w] == '#':
                cnt += 1
                ans[h][w] = cnt
                flag = True

    for h in range(H):
        flag = False
        for w in range(W-1,-1,-1):
            if flag and ans[h][w] == 0:
                ans[h][w] = cnt
            if S[h][w] == '#':
                cnt = ans[h][w]
                flag = True


    for w in range(W):
        for h in range(H-1):
            if ans[h][w] == 0:
                for h2 in range(h,H):
                    if ans[h2][w] != 0:
                        ans[h][w] = ans[h2][w]
                        break

    for w in range(W):
        for h in range(H-1,0,-1):
            if ans[h][w] == 0:
                for h2 in range(h,-1,-1):
                    if ans[h2][w] != 0:
                        ans[h][w] = ans[h2][w]
                        break


                
    for i in range(H):
        print(*ans[i])

    



if __name__ == "__main__":
    main()