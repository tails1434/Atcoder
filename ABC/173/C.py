def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    zenbu = 0
    for h in range(H):
        for w in range(W):
            if C[h][w] == '#':
                zenbu += 1
    
    if K > zenbu:
        print(0)
        exit()
    ans = 0
    for h in range(2 ** H):
        yoko = []
        for i in range(H):
            if ((h >> i) & 1):
                yoko.append(i)

        for w  in range(2 ** W):
            tate = []

            for j in range(W):
                if (w >> j) & 1:
                    tate.append(j)
            tmp = 0
            for k in range(H):
                for l in range(W):
                    if k in yoko:
                        continue
                    if l in tate:
                        continue
                    if C[k][l] == '#':
                        tmp += 1
            if tmp == K:
                ans += 1

    print(ans)
        




if __name__ == "__main__":
    main()