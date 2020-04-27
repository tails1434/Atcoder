from collections import defaultdict

import heapq
import sys

input = sys.stdin.readline

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    d = [[float("inf")]*N for i in range(N)]
    for i in range(N-1):
        d[i][i+1] = 1
        d[i+1][i] = 1

    d[X][Y] = 1
    d[Y][X] = 1
    e = defaultdict(int)
    for i in range(N):
        for j in range(i,N):
            if i == j:
                continue
            tmp = min(j - i, abs(X-i) + 1 + abs(Y-j))
            e[tmp] += 1
    for i in range(1,N):
        print(e[i])






if __name__ == "__main__":
    main()