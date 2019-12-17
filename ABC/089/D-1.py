import sys
input = sys.stdin.readline

def main():
    H, W, D = map(int, input().split())
    A = list(list(map(int, input().split())) for _ in range(H))
    Q = int(input())
    B = [(0,0)] * (H * W + 5)
    for h in range(H):
        for w in range(W): 
            B[A[h][w]] = (h+1, w+1)


    C = [0] * (H * W + 5)
    for i in range(H * W + 1):
        if i // D == 0:
            continue
        tmp = abs(B[i][0] - B[i-D][0]) + abs(B[i][1] - B[i-D][1]) 
        C[i] = tmp + C[i - D]

    for _ in range(Q):
        L, R = map(int, input().split())
        print(C[R] - C[L])


if __name__ == "__main__":
    main()