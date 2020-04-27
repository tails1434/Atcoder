import sys
sys.setrecursionlimit(4100000)
from collections import deque

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    visited = [[float('inf')] * W for _ in range(H)]
    if S[0][0] == '#':
        visited[0][0] = 1
    else:
        visited[0][0] = 0
    
    for h in range(H):
        for w in range(W):
            if h + 1 > H - 1 and w + 1 > W - 1:
                continue
            if S[h][w] == '.':
                if h + 1 > H - 1:
                    if S[h][w + 1] == '.':
                        visited[h][w+1] = min(visited[h][w], visited[h][w+1])
                    else:
                        visited[h][w+1] = min(visited[h][w] + 1,visited[h][w+1])
                elif w + 1 > W - 1:
                    if S[h+1][w] == '.':
                        visited[h+1][w] = min(visited[h][w],visited[h+1][w])
                    else:
                        visited[h+1][w] = min(visited[h][w] + 1,visited[h+1][w])
                else:
                    if S[h + 1][w] == '.':
                        visited[h+1][w] = min(visited[h][w],visited[h+1][w])
                    else:
                        visited[h+1][w] = min(visited[h][w] + 1,visited[h+1][w])

                    if S[h][w + 1] == '.':
                        visited[h][w+1] = min(visited[h][w],visited[h][w+1])
                    else:
                        visited[h][w+1] = min(visited[h][w] + 1,visited[h][w+1])

            else:
                if h + 1 > H - 1:
                    visited[h][w+1] = min(visited[h][w],visited[h][w+1])
                elif w + 1 > W - 1:
                    visited[h+1][w] = min(visited[h][w],visited[h+1][w])
                else:
                    visited[h][w+1] = min(visited[h][w],visited[h][w+1])
                    visited[h+1][w] = min(visited[h][w],visited[h+1][w])

    print(visited[H-1][W-1])


if __name__ == "__main__":
    main()