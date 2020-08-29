from collections import defaultdict

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    d = defaultdict(int)

    for h in range(H):
        for w in range(W):
            d[A[h][w]] += 1
            d[A[h][w]] %= 4

    e = defaultdict(int)
    for a in d.values():
        e[a] += 1

    if H % 2 == 0 and W % 2 == 0:
        if e[1] or e[2] or e[3]:
            print('No')
        else:
            print('Yes')
    elif H % 2 == 1 and W % 2 == 1:
        if e[1] + e[3] == 1:
            if e[2] <= (H // 2 + W // 2):
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        if e[1] or e[3]:
            print('No')
        else:
            if H % 2 == 0:
                cnt = H // 2
            else:
                cnt = W // 2
            if e[2] <= cnt:
                print('Yes')
            else:
                print('No')




if __name__ == "__main__":
    main()