from collections import defaultdict

def main():
    H, W = map(int, input().split())
    A = list(list(input()) for _ in range(H) )
    d = defaultdict(int)
    for h in range(H):
        for w in range(W):
            d[A[h][w]] += 1

    odd = 0
    even = 0
    if H % 2 and W % 2:
        odd += 1
    if H % 2:
        even += W // 2
    if W % 2:
        even += H // 2

    for key, value in d.items():
        value %= 4
        if value % 2:
            odd -= 1
            value -= 1
        if value == 2:
            even -= 1
        if even < 0 or odd < 0:
            break

    if even < 0 or odd < 0:
        print('No')
    else:
        print('Yes')
        


if __name__ == "__main__":
    main()