from collections import deque

def main():
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    d = deque()
    for i in range(N):
        for a in range(A[i]):
            d.append(i+1)
    C = [[0] * W for _ in range(H)]

    for h in range(H):
        if h % 2 == 0:
            for w in range(W):
                C[h][w] = d.popleft()
        else:
            for w in range(W-1,-1,-1):
                C[h][w] = d.popleft()
    
    for h in range(H):
        print(*C[h])


if __name__ == "__main__":
    main()