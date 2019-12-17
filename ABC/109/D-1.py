def main():
    H, W = map(int, input().split())
    A = list(list(map(int, input().split())) for _ in range(H))
    ope = []

    for w in range(W):
        for h in range(H-1):
            if A[h][w] % 2 != 0:
                A[h+1][w] += 1
                ope.append((h+1,w+1,h+2,w+1))

    for w in range(W-1):
        if A[H-1][w] % 2 != 0:
            A[H-1][w+1] += 1
            ope.append((H,w+1,H,w+2))

    print(len(ope))
    for ans in ope:
        print(*ans)

if __name__ == "__main__":
    main()