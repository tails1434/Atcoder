def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = []
    dt = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for h in range(H):
        tmp = ''
        for w in range(W):
            if S[h][w] == '#':
                for dh, dw in dt:
                    nh = h + dh
                    nw = w + dw
                    flag = True
                    if 0 <= nh < H and 0 <= nw < W:
                        if S[nh][nw] != '#':
                            tmp += '.'
                            flag = False
                            break
                if flag:
                    tmp += '#'
            else:
                tmp += '.'
        ans.append(tmp)


    tmp = [['.'] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if ans[h][w] == '#':
                tmp[h][w] = '#'
                for dh, dw in dt:
                    nh = h + dh
                    nw = w + dw
                    if 0 <= nh < H and 0 <= nw < W:
                        tmp[nh][nw] = '#'

    if tmp == S:
        print('possible')
        for a in ans:
            print(''.join(a))
    else:
        print('impossible')


if __name__ == "__main__":
    main()